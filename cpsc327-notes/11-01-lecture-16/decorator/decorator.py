"""
Decorator using inheritance.
"""

import abc


class Component(metaclass=abc.ABCMeta):
    """
    Abstract class.
    Define the interface for objects that can have responsibilities
    added to them dynamically.
    """

    @abc.abstractmethod
    def operation(self):
        pass

class ConcreteComponent(Component):
    """
    Define an object to which additional responsibilities can be
    attached.
    """

    def operation(self):
        print("calling operation on the base component")



class Decorator(Component, metaclass=abc.ABCMeta):
    """
    Maintain a reference to a Component object and define an interface
    that conforms to Component's interface.
    """

    def __init__(self, component):
        self._component = component     # reference to inner-level component

    @abc.abstractmethod
    def operation(self):
        pass

class ConcreteDecoratorA(Decorator):
    """
    Add responsibilities to the component.
    """

    def operation(self):
        # ...
        print("decorated by A")         # added functionality
        self._component.operation()     # functionality of inner-level component
        # ...

class ConcreteDecoratorB(Decorator):
    """
    Add responsibilities to the component.
    """

    def operation(self):
        # ...
        print("decorated by B")
        self._component.operation()
        # ...


def main():
    # create a base component
    concrete_component = ConcreteComponent()

    # decorate the base component
    concrete_decorator_a = ConcreteDecoratorB(ConcreteDecoratorA(concrete_component))
    concrete_decorator_b = ConcreteDecoratorB(concrete_decorator_a)

    # run operation() on the decorated component
    concrete_decorator_b.operation()

    # Output:
    # decorated by B
    # decorated by B
    # decorated by A
    # calling operation on the base component


if __name__ == "__main__":
    main()