"""
Adapter lets classes work together that couldn't otherwise because of
incompatible interfaces.
"""

import abc


class Target(metaclass=abc.ABCMeta):
    """
    Define the domain-specific interface that Client uses.
    """

    @abc.abstractmethod
    def request(self):
        pass


class Adapter(Target):
    """
    Adapt the interface of Adaptee to the Target interface.
    """

    def __init__(self, a=None, *args, **kwargs):
        if not a:
            self._adaptee = Adaptee()
        else:
            self._adaptee = a
        super().__init__(*args, **kwargs)
        

    def request(self):
        self._adaptee.specific_request()


class Adaptee:
    """
    Define an existing interface that needs adapting.
    """

    def specific_request(self):
        pass


def main():
    adapter = Adapter()
    adapter.request()


if __name__ == "__main__":
    main()