import datetime
from Bank import Bank
import sys
import pickle
from decimal import ROUND_HALF_UP, Decimal, getcontext, InvalidOperation
from Exceptions import OverdrawError, TransactionLimitError, TransactionSequenceError
import logging

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
        while (True):
            try:
                deposit = Decimal(input("Initial deposit amount?\n>"))
            except InvalidOperation:
                print("Please try again with a valid dollar amount.")
            else:
                break

        # Open account
        try:
            self._bank.openAccount(type, deposit)
        except OverdrawError:
            # Overdrawing the account (negative innitial deposit)
            # Note that the account will still be created, just with initial balance of 0 and no transactions.
            print("This transaction could not be completed due to an insufficient account balance.")


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
        
        try:
            acc.listTransactions()
        except AttributeError:
            # No account is currently selected
            print("This command requires that you first select an account.")


    def _addTransaction(self):
        """Add a transaction."""

        # Input amount
        while (True):
            try:
                amount = Decimal(input("Amount?\n>"))
            except InvalidOperation:
                print("Please try again with a valid dollar amount.")
            else:
                break

        # Input date
        while (True):
            try:
                date = datetime.datetime.strptime(input("Date? (YYYY-MM-DD)\n>"), "%Y-%m-%d").date()
            except ValueError:
                print("Please try again with a valid date in the format YYYY-MM-DD.")
            else:
                break

        # Get currently selected account
        acc = self._bank.getSelectedAccount()

        try:
            acc.addTransaction(amount, date = date)
        except AttributeError:
            # No account is currently selected
            print("This command requires that you first select an account.")
        except OverdrawError:
            # Overdrawing the account
            print("This transaction could not be completed due to an insufficient account balance.")
        except TransactionLimitError:
            # Exceeding transaction limit (for savings accounts)
            print("This transaction could not be completed because the account has reached a transaction limit.")
        except TransactionSequenceError as err:
            # Out of chronological order
            print("New transactions must be from {} onward.".format(err.getLatestDate().strftime("%Y-%m-%d")))


    def _interestAndFees(self):
        """Assesses interest and fees for the current selected account.
        Interest rates are 2.5% for savings accounts and 0.15% for checking accounts."""
        acc = self._bank.getSelectedAccount()
        try:
            acc.getInterest()
        except AttributeError:
            # No account is currently selected
            print("This command requires that you first select an account.")
        except TransactionSequenceError as err:
            # Out of chronological order
            print("Cannot apply interest and fees again in the month of {}.".format(err.getLatestDate().strftime("%B")))


    def _save(self):
        """Saves the Bank object using pickle module.
        The currently selected account will not be saved."""
        
        # Remove currently selected account
        selected = None
        if self._bank.getSelectedAccount() != None:
            selected = self._bank.getSelectedAccount().getAccountID()
            self._bank.unSelectAccount()
        
        with open("bank.pickle", "wb") as f:
            pickle.dump(self._bank, f)
        
        # Add the selected account back
        if selected != None:
            self._bank.selectAccount(selected)

        # logging
        logging.debug("Saved to bank.pickle", extra={"logLevel": "DEBUG"})


    def _load(self):
        """Loads a previously saved Bank pickle."""

        with open("bank.pickle", "rb") as f:   
            self._bank = pickle.load(f)
        
        # logging: 2021-03-03 11:41:42|DEBUG|Loaded from bank.pickle
        logging.debug("Loaded from bank.pickle", extra = {"logLevel": "DEBUG"})
    

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

    # logging config
    logging.basicConfig(filename = 'bank.log', level = logging.DEBUG, 
                    format='%(asctime)s|%(logLevel)s|%(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    try:
        BankCLI().run()
    except Exception as ex:
        print("Sorry! Something unexpected happened. If this problem persists please contact our support team for assistance.")
        logging.error(repr(str(ex)))
        sys.exit(1)