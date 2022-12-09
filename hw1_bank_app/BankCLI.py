import datetime
from Bank import Bank
import sys
import pickle
from decimal import ROUND_HALF_UP, Decimal, getcontext

class BankCLI():
    """Display a menu and respond to choices."""

    def __init__(self):
        self._bank = Bank()
        self._choices = {
            "1": self._openAccount, 
            "2": self._printSummary,
            "3": self._selectAccount,
            "4": self._listTransactions,
            "5": self._addTransaction,
            "6": self._interestAndFees,
            "7": self._save,
            "8": self._load,
            "9": self._quit,
        }

    # Running commands:

    def _openAccount(self):
        """Open an account."""

        # Input account type
        print("Type of account? (checking/savings)")
        type = input(">")

        while type != "checking" and type != "savings":
            # Error: invalid input
            print("Invalid input: expecting \"checking\" or \"savings\"")
            print("Type of account? (checking/savings)")
            type = input(">")

        # Input initial deposit
        print("Initial deposit amount?")
        deposit = Decimal(input(">"))

        self._bank.openAccount(type, deposit)


    def _printSummary(self):
        """Print a summary of all accounts."""
        for acc in self._bank.allAccounts():
            print(acc)


    def _selectAccount(self):
        """Select an account by account ID."""

        # input account number
        print("Enter account number")
        id = int(input(">"))

        self._bank.selectAccount(id)


    def _listTransactions(self):
        """List all transactions of the currently selected account."""

        # Get currently selected account
        acc = self._bank.getSelectedAccount()
        if acc == None:
            # Error: no account is currently selected
            print("No account selected.")
            return

        acc.listTransactions()


    def _addTransaction(self):
        """Add a transaction."""

        # Get currently selected account
        acc = self._bank.getSelectedAccount()
        if acc == None:
            # Error: no account is currently selected
            print("No account selected.")
            return

        # Input amount
        print("Amount?")
        amount = Decimal(input(">"))

        # Input date
        print("Date? (YYYY-MM-DD)")
        date = datetime.datetime.strptime(input(">"), "%Y-%m-%d").date()

        acc.addTransaction(amount, date = date)


    def _interestAndFees(self):
        """Assesses interest and fees for all accounts.
        Interest rates are 2.5% for savings accounts and 0.15% for checking accounts."""
        self._bank.getInterest()


    def _save(self):
        """Saves the Bank object using pickle module.
        The currently selected account will not be saved."""
        
        # Remove currently selected account
        selected = None
        if self._bank.getSelectedAccount() != None:
            selected = self._bank.getSelectedAccount().getAccountID()
            self._bank.unSelectAccount()
        
        with open("bank_save.pickle", "wb") as f:
            pickle.dump(self._bank, f)
        
        # Add the selected account back
        if selected != None:
            self._bank.selectAccount(selected)


    def _load(self):
        """Loads a previously saved Bank pickle."""

        with open("bank_save.pickle", "rb") as f:   
            self._bank = pickle.load(f)
    

    def _quit(self):
        """Quit the Bank app."""

        print("Thank you for using the Bank App. Goodbye.")
        sys.exit(0)
        


    # Menu display:

    def _display_menu(self):
        """Display the menu."""

        print("--------------------------------")

        # print currently selected account
        print("Currently selected account:", self._bank.getSelectedAccount())

        # print commands:
        print("""Enter command
1: open account
2: summary
3: select account
4: list transactions
5: add transaction
6: interest and fees
7: save
8: load
9: quit"""        
        )
        
    
    # Display menu and respond to commands:
        
    def run(self):
        """Display the menu and respond to choices."""
        while True:
            self._display_menu()
            choice = input(">")
            action = self._choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    


if __name__ == "__main__":

    # Set up Decimal rounding context
    getcontext().rounding = ROUND_HALF_UP

    BankCLI().run()