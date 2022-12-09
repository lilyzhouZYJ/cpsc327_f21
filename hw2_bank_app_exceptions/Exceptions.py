class OverdrawError(Exception):    
    "This exception handles the error of overdrawing the account balance."
    pass

class TransactionLimitError(Exception):
    "This exception handles the error of exceeding the transaction limit."
    pass

class TransactionSequenceError(Exception):
    "This exception handles the error of adding transactions out of order."
    def __init__(self, latest_date):
        self._latest_date = latest_date

    def getLatestDate(self): 
        return self._latest_date