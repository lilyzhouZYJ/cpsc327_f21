from Account import Account
import datetime

class SavingsAccount(Account):
    """Represents a savings account."""

    def __init__(self, accountID):
        """Initialize a savings account"""
        super().__init__("savings", accountID)

    def addTransaction(self, amount, isInterest = False, date = datetime.date.today()):
        """Add a transaction of the given amount, on the given date."""

        if isInterest == False:
            # check if transaction limit is exceeded
            sameDay = 0
            sameMonth = 0
            for trans in self._transactions:
                if trans.isInterest() == True:
                    # interest transactions do not count towards the transaction limit
                    continue

                if trans.getDate() == date:
                    sameDay += 1
                    if sameDay >= 2:         # daily transaction limit exceeded
                        return
                if trans.getDate().month == date.month:
                    sameMonth += 1
                    if sameMonth >= 5:       # monthly transaction limit exceeded
                        return
        
        super().addTransaction(amount, isInterest = isInterest, date = date)