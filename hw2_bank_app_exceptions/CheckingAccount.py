from Account import Account
from decimal import Decimal
import datetime
import calendar

class CheckingAccount(Account):
    """Represent a checking account."""

    def __init__(self, accountID):
        """Initialize a checking account"""
        super().__init__("checking", accountID)

    def getInterest(self):
        """Assesses interest and fee for the account.
        If the balance is less than $100, will add a $10 fee."""

        if(self._latestTransDate == None):
            # no transaction exists
            return

        # add interest transaction
        super().getInterest()

        date = self._getInterestDate()

        # assess fee
        if self._balance < 100:
            fee = Decimal(-10)
            super().addTransaction(fee, isInterest = True, date = date)