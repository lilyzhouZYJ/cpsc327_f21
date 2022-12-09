from Account import Account
from decimal import Decimal

class CheckingAccount(Account):
    """Represent a checking account."""

    def __init__(self, accountID):
        """Initialize a checking account"""
        super().__init__("checking", accountID)

    def getInterest(self):
        """Assesses interest and fee for the account.
        If the balance is less than $100, will add a $10 fee."""

        # add interest transaction
        super().getInterest()

        # assess fee
        if self._balance < 100:
            fee = Decimal(-10)
            super().addTransaction(fee, isInterest = True)