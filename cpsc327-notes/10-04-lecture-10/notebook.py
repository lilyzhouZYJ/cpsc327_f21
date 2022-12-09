from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import functools

from sqlalchemy.types import TypeDecorator

# declarative_base(): function from sqlalchemy, returns a class
# allows us to return our tables from our classes
Base = declarative_base()



class MyTime(TypeDecorator):
    # Decorator: design pattern - wrap up some code so whenever we
    # use it, some extra stuff is run
    "Convert datetime to strings and vice versa."

    impl = String

    def __init__(self, length=None, format="%Y-%m-%d", **kwargs):
        super().__init__(length, **kwargs)
        self.format = format

    def process_literal_param(self, value, dialect):
        # allow passing string or time to column
        if isinstance(value, str):
            value = datetime.strptime(value, self.format).time()

        # convert python time to sql string
        return value.strftime(self.format) if value is not None else None

    process_bind_param = process_literal_param

    def process_result_value(self, value, dialect):
        # convert sql string to python time
        return datetime.strptime(value, self.format).date() if value is not None else None




class Notebook(Base):
    """Represent a collection of notes that can be tagged,
    modified, and searched."""

    __tablename__ = "notebook"      # notebook class mapped to notebook table

    _id = Column(Integer, primary_key=True) # id: primary key for the table
                                            # primary_key: automatically counts up from 1
    
    # relationship: replaces list of Notes, we can treat _notes as array
    # when we add to _notes, it will convert to sql query
    # backref is unnecessary, but useful for the example:
    # can use the parent "notebook" in the Note class
    _notes = relationship("Note", backref=backref("notebook")) 


    # replace initializer with the relationship() above
    # def __init__(self):
    #     """Initialize a notebook with an empty list."""
    #     self._notes = []

    def new_note(self, memo, session, tags=""):
        """Create a new note and add it to the list."""
        n = Note(memo, tags)
        self._notes.append(n)   # still use append to add to _notes
        session.add(n)

        

    def _find_note(self, note_id):
        """Locate the note with the given id."""
        for note in self._notes:            # can still iterate through _notes
            if note.id_matches(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo, session):
        """Find the note with the given id and change its
        memo to the given value."""
        note = self._find_note(note_id)
        if note:
            note.update_memo(memo)
            session.add(note)       # add is not necessarily create; just sync the updated note
            return True
        return False

    def modify_tags(self, note_id, tags, session):
        """Find the note with the given id and change its
        tags to the given value."""
        note = self._find_note(note_id)
        if note:
            note.update_tags(tags)
            session.add(note)
            return True
        return False

    def search(self, filter):
        """Find all notes that match the given filter
        string."""
        return [note for note in self._notes if note.match(filter)]

    def all_notes(self):
        """Returns all notes in the notebook"""

        # could be sorted as below, or organized some other way
        return sorted(self._notes)




@functools.total_ordering
class Note(Base):
    """Represent a note in the notebook. Match against a
    string in searches and store tags for each note."""

    # Store the next available id for all new notes
    __tablename__ = "note"

    # class variables: Column objects
    _id = Column(Integer, primary_key=True)
    _notebook_id = Column(Integer, ForeignKey("notebook._id"))
    # foreignKey: associates primary key _id above with the _id in the notebook table
    # i.e. _notebook_id will be a column of id's from the notebook table
    _memo = Column(String)
    _tags = Column(String)
    _creation_date = Column(MyTime(length=10))
    # MyTime class converts datetime objects to strings and vice versa
    # because there are no datatypes for time in SQL

    # last_id = 0

    def __init__(self, memo, tags=""):
        """initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id."""

        # instance variables: fill in rows of the table
        self._memo = memo
        self._tags = tags
        self._creation_date = datetime.today()

        # Note.last_id += 1
        # self._id = Note.last_id


    def match(self, filter):
        """Determine if this note matches the filter
        text. Return True if it matches, False otherwise.

        Search is case sensitive and matches both text and
        tags."""

        return filter in self._memo or filter in self._tags

    def id_matches(self, id):
        """
        Determine if this note has the given id
        """
        return self._id == int(id)

    def update_memo(self, memo):
        self._memo = memo

    def update_tags(self, tags):
        self._tags = tags

    def __str__(self):
        return f"{self._id}: {self._memo}\n{self._tags}"

    def __lt__(self, other):
        return self._id < other._id

    def __eq__(self, other):
        return self._id == other._id


if __name__ == "__main__":

    engine = create_engine(f"sqlite:///notebook.db")
    Base.metadata.create_all(engine)