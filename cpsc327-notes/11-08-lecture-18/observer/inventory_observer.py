class Inventory:
    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0

    def attach(self, observer):
        self.observers.append(observer)


    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
        self._update_observers()

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self._update_observers()

    def _update_observers(self):
        for observer in self.observers:
            observer()      # update observer by calling it


class ConsoleObserver:
    def __init__(self, inventory):
        self.inventory = inventory

    def __call__(self):     # update observer using __call__()
        print(self.inventory.product)
        print(self.inventory.quantity)

i = Inventory()

o = ConsoleObserver(i)

i.attach(o)

i.product = "Computer"
i.quantity = 10

i.quantity -= 1