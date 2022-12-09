"""
Define a family of algorithms, encapsulate each one, and make them
interchangeable. Strategy lets the algorithm vary independently from
clients that use it.
"""

import abc


class Context:
    """
    Define the interface of interest to clients.
    Maintain a reference to a Strategy object.
    """

    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        self._strategy()


class Strategy(metaclass=abc.ABCMeta):
    """
    Declare an interface common to all supported algorithms. Context
    uses this interface to call the algorithm defined by a
    ConcreteStrategy.
    """

    @abc.abstractmethod
    def __call__(self):
        pass


class ConcreteStrategyA(Strategy):
    """
    Implement the algorithm using the Strategy interface.
    """

    def __call__(self):
        print("A")


class ConcreteStrategyB(Strategy):
    """
    Implement the algorithm using the Strategy interface.
    """

    def algorithm_interface(self):
        print("B")

def strategy_a():
    print("A")

def strategy_b():
    print("B")

def main():
    # concrete_strategy_a = ConcreteStrategyA()
    # context = Context(concrete_strategy_a)
    # context.context_interface()

    # context._strategy = ConcreteStrategyB()
    # context.context_interface()


    # Could also just use functions
    context = Context(strategy_b)
    context2 = strategy_a

    context2()

    context2 = strategy_b
    context2()


if __name__ == "__main__":
    main()