"""
Decorator using class decorator annotation (@decorator syntax).
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




class Decorator(Component, metaclass=abc.ABCMeta):
    """
    Maintain a reference to a Component object and define an interface
    that conforms to Component's interface.
    """

    def __init__(self, klass):
        # passing in a class decoration
        # note: using 'klass' to avoid clash with reserved word 'clash'
        self._klass = klass

    @abc.abstractmethod
    def operation(self):
        pass

    def __call__(self):
        self._component = self._klass()
        return self

class ConcreteDecoratorA(Decorator):
    """
    Add responsibilities to the component.
    """

    def operation(self):
        # ...
        print("decorated by A")
        self._component.operation()
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




# ConcreteComponent will first get passed to the constructor of ConcreteDecoratorA;
# the resulting object is then called (meaning __call__() of Decorator class is triggered).
# These steps result in a ConcreteDecoratorA object, with self._klass as ConcreteComponent
# and self._component as a ConcreteComponent object.

# The ConcreteDecoratorA object is then passed to the constructor of ConcreteDecoratorB,
# and the same steps are repeated there. 
# These steps result in a ConcreteDecoratorB object, with self._klass as ConcreteDecoratorA
# and self._component as a ConcreteDecoratorA object.

@ConcreteDecoratorB
@ConcreteDecoratorA
class ConcreteComponent(Component):
    """
    Define an object to which additional responsibilities can be
    attached.
    """

    def operation(self):
        print("calling operation on the base component")


def main():
    concrete_component = ConcreteComponent()

    print(concrete_component)
    # output: <__main__.ConcreteDecoratorB object at 0x000001C6E58927C0>

    print(dir(concrete_component))
    # output includes '_component', '_klass', 'operation'

    print(concrete_component._component)
    # output: <__main__.ConcreteDecoratorA object at 0x0000024EF2E925E0>

    print(concrete_component._component._component)
    # output: <__main__.ConcreteComponent object at 0x000001C6E5892850>

    concrete_component.operation()
    # output:
    # decorated by B
    # decorated by A
    # calling operation on the base component



if __name__ == "__main__":
    main()