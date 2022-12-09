from Transaction import Transaction
from decimal import Decimal
import datetime

class Account():

    """Represents an account. Stores an account type, balance, account ID,
    as well as a list of transactions."""\

    def __init__(self, accountType, accountID):
        self._accountID = accountID
        self._accountType = accountType
        self._balance = Decimal(0)
        self._transactions = []

    def __str__(self):
        """Print account summary in the format of:
        [AccountType]#[AccountID, padded to 9 digits], \\t balance: $[balance]"""
        return "{}#{:09d},\tbalance: ${:,.2f}".format(self._accountType.capitalize(), self._accountID, self._balance)

    def getBalance(self):
        """Returns the current balance of the account."""
        return self._balance

    def getAccountID(self):
        """Returns the account ID of the account."""
        return self._accountID


    def addTransaction(self, amount, isInterest = False, date = datetime.date.today()):
        """Add a transaction of the given amount, on the given date."""

        newBalance = self._balance + amount
        if isInterest == False and newBalance < 0 and amount < 0:
            # overdrawing the account
            return
        
        # Process the transaction
        self._balance = newBalance
        trans = Transaction(amount, date = date, isInterest = isInterest)
        self._transactions.append(trans)


    def listTransactions(self):
        """List all the transactions of the account."""
        transactions = sorted(self._transactions)
        for trans in transactions:
            print(trans)

    def getInterest(self):
        """Calculate interest for the account."""
        if self._accountType == "savings":
            rate = Decimal(0.025)
        elif self._accountType == "checking":
            rate = Decimal(0.0015)
        
        interest = self._balance * rate
        self.addTransaction(interest, isInterest = True)

