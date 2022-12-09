"""
Define a one-to-many dependency between objects so that when one object
changes state, all its dependents are notified and updated automatically.
"""

import abc


class Subject:
    """
    Know its observers. Any number of Observer objects may observe a
    subject.
    Send a notification to its observers when its state changes.
    """

    def __init__(self):
        self._observers = set()
        self._subject_state = None
        self._name = "MyName"
        self._age = 15

    def attach(self, observer):
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update()

    @property
    def subject_state(self):
        return self._subject_state

    @subject_state.setter
    def subject_state(self, arg):
        self._subject_state = arg
        self._notify()          # notify observers

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, arg):
        self._age = arg
        self._notify()          # notify observers


class Observer(metaclass=abc.ABCMeta):
    """
    Define an updating interface for objects that should be notified of
    changes in a subject.
    """

    def __init__(self):
        self._subject = None            # reference to subject
        self._observer_state = None

    @abc.abstractmethod
    def update(self):
        pass


class ConcreteObserver(Observer):
    """
    Implement the Observer updating interface to keep its state
    consistent with the subject's.
    Store state that should stay consistent with the subject's.
    """

    def update(self):           # pull data from subject
        self._observer_state = self._subject.subject_state
        print(f"Observer {self} sees: {self._observer_state}")

class AgeObserver(Observer):
    """
    Implement the Observer updating interface to keep its state
    consistent with the subject's.
    Store state that should stay consistent with the subject's.
    """

    def update(self):           # pull data from subject
        self._observer_state = self._subject.age
        print(f"Observer {self} sees: {self._observer_state}")


def main():
    subject = Subject()
    concrete_observer = ConcreteObserver()
    concrete_observer2 = ConcreteObserver()
    subject.attach(concrete_observer)
    subject.attach(concrete_observer2)
    subject.attach(AgeObserver())
    subject.subject_state = 123
    subject.age += 1


if __name__ == "__main__":
    main()