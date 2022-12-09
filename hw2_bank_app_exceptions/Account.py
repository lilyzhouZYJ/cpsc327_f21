from Exceptions import OverdrawError, TransactionSequenceError
from Transaction import Transaction
from decimal import Decimal
import datetime
import calendar
import logging

class Account():

    """Represents an account. Stores an account type, balance, account ID,
    as well as a list of transactions."""\

    def __init__(self, accountType, accountID):
        self._accountID = accountID
        self._accountType = accountType
        self._balance = Decimal(0)
        self._transactions = []
        self._latestTransDate = None        # the date of the latest transaction (including interest/fees)
        self._latestInterest = False        # has the interest/fee been added for the month of the latest transaction?

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
            raise OverdrawError()
        
        if(self._latestTransDate != None and date < self._latestTransDate):
            # out of chronological order
            raise TransactionSequenceError(latest_date = self._latestTransDate)

        # Process the transaction
        self._balance = newBalance
        trans = Transaction(amount, date = date, isInterest = isInterest)
        self._transactions.append(trans)

        if(isInterest == True):
            self._latestInterest = True
        else:
            # new transaction in a new month?
            if(self._latestInterest == True and date.month > self._latestTransDate.month):
                self._latestInterest = False

        # update date of latest transaction
        self._latestTransDate = date

        # logging:
        logging.debug("Created transaction: {}, {}".format(self.getAccountID(), amount), extra={"logLevel": "DEBUG"})


    def listTransactions(self):
        """List all the transactions of the account."""
        transactions = sorted(self._transactions)
        for trans in transactions:
            print(trans)

    def _getInterestDate(self):
        """Get the last day of the month of the latest transaction."""
        lastTrans = self._latestTransDate
        lastDay = calendar.monthrange(lastTrans.year, lastTrans.month)[1]
        date = datetime.date(lastTrans.year, lastTrans.month, lastDay)
        return date

    def _hasAddedInterest(self, date):
        """Checks if interest/fees have already been added for the month of the latest transaction."""
        if(date.month == self._latestTransDate.month and self._latestInterest == True):
            return True
        return False

    def getInterest(self, date = None):
        """Calculate interest for the account."""
        if(self._latestTransDate == None):
            # no transaction exists
            return

        if self._accountType == "savings":
            rate = Decimal(0.025)
        elif self._accountType == "checking":
            rate = Decimal(0.0015)
        
        interest = self._balance * rate

        date = self._getInterestDate()
        if(self._hasAddedInterest(date) == True):
            # interest has already been added
            raise TransactionSequenceError(latest_date = self._latestTransDate)

        self.addTransaction(interest, isInterest = True, date = date)

        # logging
        logging.debug("Triggered fees and interest", extra={"logLevel": "DEBUG"})

