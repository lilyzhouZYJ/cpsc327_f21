import tkinter as tk
import sys
import pickle
from notebook import Notebook


class Menu:
    """Display a menu and respond to choices when run."""

    def __init__(self):
        
        self._window = tk.Tk()
        self._window.title("MY NOTEBOOK")

        self._notebook = Notebook()
        self._options_frame = tk.Frame(self._window)        # frame for options

        # creating button objects rather than mapping options to functions
        tk.Button(self._options_frame, 
                text="Show all Notes", 
                command=self._show_notes).grid(row=1, column=1, columnspan=2)
                # command argument: attaches the _show_notes callback to the button
        tk.Button(self._options_frame, 
                text="Search Notes", 
                command=self._search_notes).grid(row=1, column=3)
        tk.Button(self._options_frame, 
                text="Add Note", 
                command=self._add_note).grid(row=1, column=4)
        tk.Button(self._options_frame, 
                text="Modify Note", 
                command=self._modify_note).grid(row=1, column=5)
        tk.Button(self._options_frame, 
                text="Save", 
                command=self._save).grid(row=1, column=6)
        tk.Button(self._options_frame, 
                text="Load", 
                command=self._load).grid(row=1, column=7)

        self._list_frame = tk.Frame(self._window)           # frame of list of notes
        self._note_frame = tk.Frame(self._window)           # frame of note
        self._options_frame.grid(row=0, column=1, columnspan=2)
        self._list_frame.grid(row=1, column=1, columnspan=1, sticky="w")
        self._note_frame.grid(row=1, column=2, columnspan=1)

        self._notes = {}

        self._window.mainloop()



    def _show_notes(self, notes=None):
        if not notes:
            notes = self._notebook.all_notes()
        row = 0
        for x in notes:
            if x._id not in self._notes:
                # sets up a dictionary of StringVars associated with the buttons created
                self._notes[x._id] = tk.StringVar(value=str(x))
                tk.Button(self._list_frame, text=x, textvariable=self._notes[x._id], command=lambda note=x: self._modify_note(note)).grid(row=row, column=1)
            else:
                # reuse the old button, but set the StringVar to change its label
                self._notes[x._id].set(str(x))
            row += 1

        # #another way to do this would be to delete all of the buttons and recreate a new set with the the proper text
        # for x in self._list_frame.winfo_children():
        #     #get all the widgets in the frame and destroy them
        #     x.destroy()
        # row = 0
        # for x in notes:
        #     # note: if instead of using "lambda note=x : self._modify_note(note)", we use
        #     # "lambda : self._modify_note(x)", then it will look for x outside the scope of the
        #     # function ONLY when this callback is called, meaning that at that point, x will be
        #     # the last note.
        #     tk.Button(self._list_frame, text=x, command=lambda note=x: self._modify_note(note)).grid(row=row, column=1)
        #     row += 1


        

    def _search_notes(self):
        filter = input("Search for: ")
        notes = self._notebook.search(filter)
        self._show_notes(notes)

    def _add_note(self):
        def add():
            self._notebook.new_note(e1.get())
            e1.destroy()
            b.destroy()
            l1.destroy()
            self._show_notes()


        l1 = tk.Label(self._options_frame, text="Memo:")
        l1.grid(row=2, column=1)
        e1 = tk.Entry(self._options_frame)
        e1.grid(row=3, column=1)

        b = tk.Button(self._options_frame, text="Enter", command=add)
        b.grid(row=3, column=2)



    def _modify_note(self, note):

        def add():
            note.update_memo(e1.get())
            note.update_tags(e2.get())
            e1.destroy()
            e2.destroy()
            l1.destroy()
            l2.destroy()
            b.destroy()
            self._show_notes()

        l1 = tk.Label(self._options_frame, text="Memo:")
        l2 = tk.Label(self._options_frame, text="Tags:")
        e1 = tk.Entry(self._options_frame)
        e2 = tk.Entry(self._options_frame)
        b = tk.Button(self._options_frame, text="Enter", command=add)
        e1.grid(row=3, column=3)
        l1.grid(row=2, column=3)
        e2.grid(row=3, column=4)
        l2.grid(row=2, column=4)
        b.grid(row=3, column=5)



    def _save(self):
        with open("notebook_save.pickle", "wb") as f:
            pickle.dump(self._notebook, f)

    def _load(self):
        with open("notebook_save.pickle", "rb") as f:   
            self._notebook = pickle.load(f)



if __name__ == "__main__":
    Menu()