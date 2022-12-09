class OutOfStock(Exception):
    "This exception should be raised when an inventory object does not have any more items of a particular type"
    pass


class InvalidItemType(Exception):
    pass


class Inventory:
    def lock(self, item_type):
        """Select the type of item that is going to
        be manipulated. This method will lock the
        item so nobody else can manipulate the
        inventory until it's returned. This prevents
        selling the same item to two different
        customers."""
        pass

    def unlock(self, item_type):
        """Release the given type so that other
        customers can access it."""
        pass

    def purchase(self, item_type):
        """If the item is not locked, raise an
        exception. If the item_type  does not exist,
        raise an exception. If the item is currently
        out of stock, raise an exception. If the item
        is available, subtract one item and return
        the number of items left."""
        if (self.count(item_type) < 1):
            raise OutOfStock()


item_type = "widget"
inv = Inventory()
inv.lock(item_type)
try:
    num_left = inv.purchase(item_type)
except InvalidItemType:
    print("Sorry, we don't sell {}".format(item_type))
except OutOfStock:
    print("Sorry, that item is out of stock.")
else:
    # no exceptions
    print(
    "Purchase complete. There are "
    "{} {}s left".format(num_left, item_type)
)
finally:
    # this will always run
    inv.unlock(item_type)

