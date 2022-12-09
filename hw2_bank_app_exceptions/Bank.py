from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount
from Account import Account
import logging

class Bank():

    def __init__(self):
        """Initialize bank with empty list of accounts, and no account is
        currently selected."""
        self._accounts = []
        self._selectedAccount = None
        self._nextID = 1            # this is used to generate account IDs

    def allAccounts(self):
        """Return list of all accounts."""
        return self._accounts

    def openAccount(self, accountType, initDeposit):
        """Open an account of the given account type, with the given initial deposit."""
        # Create account
        if accountType == "checking":
            acc = CheckingAccount(self._nextID)
        elif accountType == "savings":
            acc = SavingsAccount(self._nextID)
        self._accounts.append(acc)
        self._nextID += 1

        # logging
        logging.debug("Created account: {}".format(acc.getAccountID()), extra={"logLevel": "DEBUG"})

        # Add initial deposit on current date
        acc.addTransaction(initDeposit)

        
        
    def getSelectedAccount(self):
        """Return the currently selected account."""
        return self._selectedAccount
    
    def selectAccount(self, accountID):
        """Set the account with the given accountID as the currenbtly
        selected account."""
        selected = None
        for acc in self._accounts:
            if acc.getAccountID() == accountID:
                selected = acc
        
        if selected == None:
            # Error: no account of the given account ID was found
            return
        else:
            self._selectedAccount = selected

    def unSelectAccount(self):
        """Set the selected account to None, so that no account is selected."""
        self._selectedAccount = None
            
        