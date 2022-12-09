
from pickle import FALSE


class Transaction():

    """Represents a transaction. Stores the transaction amount and date."""

    def __init__(self, amount, date, isInterest = False):
        self._date = date
        self._amount = amount
        self._isInterest = isInterest       # is this transaction for interest?
    
    def getDate(self):
        """Returns the date of the transaction."""
        return self._date

    def getAmount(self):
        """Returns the amount of the transaction."""
        return self._amount

    def isInterest(self):
        """Returns whether this transaction is for interest or fee."""
        return self._isInterest

    def __str__(self):
        """Display transaction information in the format:
        2021-09-05, $50.00"""
        return "{}, ${:,.2f}".format(self._date.strftime("%Y-%m-%d"), round(self._amount, 2))

    def __lt__(self, other):
        return self._date < other._date

    def __eq__(self, other):
        return self._date == other._date