import logging
import sys
from decimal import Decimal, InvalidOperation
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import sqlalchemy
from sqlalchemy.orm.session import sessionmaker

from Bank import Bank, Base
from Accounts import OverdrawError, TransactionLimitError, TransactionSequenceError




logging.basicConfig(filename='bank.log', level=logging.DEBUG, format='%(asctime)s|%(levelname)s|%(message)s', datefmt='%Y-%m-%d %H:%M:%S')





class BankGUI():

    @staticmethod
    def handle_exception(exception, value, traceback):
        "Handles exception."
        messagebox.showwarning(title="Error", message="Sorry! Something unexpected happened. If this problem persists please contact our support team for assistance.")
        logging.error(str(e.__class__.__name__) + ": " + repr(str(e)))
        sys.exit(1)


    def __init__(self):
        # session
        self._session = Session()

        # pull in data from session
        self._bank = self._session.query(Bank).first()
        if not self._bank:
            self._bank = Bank()
            self._session.add(self._bank)
            self._session.commit()
            logging.debug("Saved to bank.db")
        else :
            logging.debug("Loaded from bank.db")

        # set up tkinter window + frame
        self._window = tk.Tk()
        self._window.title("MY BANK")
        self._options_frame = tk.Frame(self._window)        # menu options
        self._input_frame = None                            # inputing things
        self._list_frame = tk.Frame(self._window)           # list of accounts
        self._transactions_frame = None                     # account transactions

        self._window.report_callback_exception = BankGUI.handle_exception   # handle errors

        # dictionary matching account numbers to displayed account widgets
        self._acc_widgets = {}

        # account ID of selected account
        self._selected_account = tk.IntVar()

        # creating buttons for options
        tk.Button(self._options_frame, 
                text="open account", 
                command=self._open_account).grid(row=0, column=0, columnspan=2, ipadx=10, ipady=3)
        tk.Button(self._options_frame, 
                text="add transaction", 
                command=self._add_transaction).grid(row=0, column=2, columnspan=2, ipadx=10, ipady=3)
        tk.Button(self._options_frame, 
                text="interest and fees", 
                command=self._monthly_triggers).grid(row=0, column=4, columnspan=2, ipadx=10, ipady=3)

        # place frames        
        self._options_frame.grid(row=0, column=0)
        self._list_frame.grid(row=2, column=0)

        self._summary()

        self._window.mainloop()





    def _add_transaction(self):
        "Add new transaction."

        if(self._input_frame is not None):
            self._input_frame.destroy()

        # create input frame
        self._input_frame = tk.Frame(self._window)
        self._input_frame.grid(row=1, column=0)

        def check_amount_format(*args):
            "Checks if the amount input format is valid."
            inputStr = amount.get()
            if(len(inputStr) == 0):
                # empty input
                amtEntry.config({"background": "White"})
            else:
                try:
                    Decimal(amount.get())
                except InvalidOperation:
                    amtEntry.config({"background": "Red"})
                    return False
                else:
                    amtEntry.config({"background": "White"})
                    return True

        def check_date_format(*args):
            "Checks if the date input format is valid."
            inputStr = date.get()
            if(len(inputStr) == 0):
                # empty input
                dateEntry.config({"background": "White"})
            else:
                try:
                    datetime.strptime(inputStr, "%Y-%m-%d").date()
                except ValueError:
                    dateEntry.config({"background": "Red"})
                    return False
                else:
                    dateEntry.config({"background": "White"})
                    return True

        def add_transaction():
            "Add transaction."
            # check validity of inputs
            if not check_amount_format():
                self._popup_error("Please input a valid amount.")
                return
            if not check_date_format():
                self._popup_error("Please input a valid date.")
                return

            try:
                myAmount = Decimal(amount.get())
                myDate = datetime.strptime(date.get(), "%Y-%m-%d").date()
                accNum = self._selected_account.get()
                self._bank.get_account(accNum).add_transaction(myAmount, self._session, myDate)
            except AttributeError:
                # no account selected
                self._popup_error("This command requires that you first select an account.")
            except OverdrawError:
                self._popup_error("This transaction could not be completed due to an insufficient account balance.")
            except TransactionLimitError:
                self._popup_error("This transaction could not be completed because the account has reached a transaction limit.")
            except TransactionSequenceError as e:
                self._popup_error(f"New transactions must be from {e.latest_date} onward.")
            else:
                self._input_frame.destroy()
                self._input_frame = None
                self._session.commit()
                logging.debug("Saved to bank.db")
                self._list_transactions(accNum)
                self._summary()

        amtLabel = tk.Label(self._input_frame, text="Amount:")
        amtLabel.grid(row=1, column=0)
        amount = tk.StringVar()
        amtEntry = tk.Entry(self._input_frame, textvariable=amount)
        amtEntry.grid(row=1, column=1)
        amount.trace(mode="w", callback=check_amount_format)

        dateLabel = tk.Label(self._input_frame, text="Date:")
        dateLabel.grid(row=2, column=0)
        date = tk.StringVar()
        dateEntry = tk.Entry(self._input_frame, textvariable=date)
        dateEntry.grid(row=2, column=1)
        date.trace(mode="w", callback=check_date_format)

        # enter button
        button = tk.Button(self._input_frame, text="Enter", command=add_transaction)
        button.grid(row=3, column=2)




    def _summary(self, accounts=None):
        "Show summary of all accounts."
        accounts = self._bank.show_accounts()
        row = 0
        for acc in accounts:
            accNum = acc.get_account_number()
            if accNum not in self._acc_widgets:
                # add the account as widget
                self._acc_widgets[accNum] = tk.StringVar(value=str(acc))
                acctButton = tk.Radiobutton(self._list_frame, textvariable=self._acc_widgets[accNum], variable=self._selected_account, value=accNum, command=lambda num=accNum: self._list_transactions(num))
                acctButton.grid(row=row, column=0)
            else:
                # reuse the old widget, but set the StringVar to change its label
                self._acc_widgets[accNum].set(str(acc))
            row += 1



    def _open_account(self):
        "Opens new account."

        if self._input_frame is not None:
            self._input_frame.destroy()

        # create frame
        self._input_frame = tk.Frame(self._window)
        self._input_frame.grid(row=1, column=0)

        def add_account():
            "Open account."
            # check inputs
            myAccType = acctType.get()
            if myAccType != "checking" and myAccType != "savings":
                self._popup_error("Please select an account type.")
                return

            try:  
                self._bank.add_account(acctType.get(), Decimal(amount.get()), self._session)
            except InvalidOperation:
                self._popup_error("Please input a valid amount.")
            except OverdrawError:
                self._popup_error("This transaction could not be completed due to an insufficient account balance.")
                self._input_frame.destroy()
                self._input_frame = None
                self._summary()
            else:
                self._input_frame.destroy()
                self._input_frame = None
                self._session.commit()
                logging.debug("Saved to bank.db")
                self._summary()

        def check_amount_format(*args):
            "Checks if the amount input format is valid."
            inputStr = amount.get()
            if(len(inputStr) == 0):
                # empty input
                entry.config({"background": "White"})
            else:
                try:
                    Decimal(amount.get())
                except InvalidOperation:
                    entry.config({"background": "Red"})
                else:
                    entry.config({"background": "White"})

        # label
        label = tk.Label(self._input_frame, text="Initial deposit:")
        label.grid(row=2, column=1)

        # get amount
        amount = tk.StringVar()
        entry = tk.Entry(self._input_frame, textvariable=amount)
        entry.grid(row=3, column=1)
        amount.trace(mode="w", callback=check_amount_format)

        # get account type
        acctType = tk.StringVar()
        acctType.set("Select account type")
        options = ["checking", "savings"]
        dropdown = tk.OptionMenu(self._input_frame, acctType, *options)
        dropdown.grid(row=4, column=1)

        # enter button
        button = tk.Button(self._input_frame, text="Enter", command=add_account)
        button.grid(row=4, column=2)



    def _monthly_triggers(self):
        "Calculate monthly interests and fees."
        if self._input_frame is not None:
            self._input_frame.destroy()
            self._input_frame = None

        try:
            accNum = self._selected_account.get()
            self._bank.get_account(accNum).assess_interest_and_fees(self._session)
            logging.debug("Triggered fees and interest")
        except AttributeError as e:
            self._popup_error("This command requires that you first select an account.")
        except TransactionSequenceError as e:
            self._popup_error(f"Cannot apply interest and fees again in the month of {e.latest_date.strftime('%B')}.")
        else:
            self._session.commit()
            logging.debug("Saved to bank.db")
            self._list_transactions(accNum)
            self._summary()



    def _list_transactions(self, accNum = None):
        "List all transactions of the selected account."
        if self._transactions_frame is not None:
            self._transactions_frame.destroy()
            self._transactions_frame = None

        # create frame
        self._transactions_frame = tk.Frame(self._window)
        self._transactions_frame.grid(row=2, column=2)

        if accNum is None:
            accNum = self._selected_account.get()
        account = self._bank.get_account(accNum)
        row = 0
        for x in account.get_transactions():
            trans = tk.Label(self._transactions_frame, text=str(x))
            if(x.is_withdrawal()):
                trans.config({"fg": "Red"})
            else :
                trans.config({"fg": "Green"})
            trans.grid(row=row, column=0)
            row += 1



    def _popup_error(self, message):
        "Pop up box with error message."
        messagebox.showwarning(title="Error", message=message)





if __name__ == "__main__":

    engine = sqlalchemy.create_engine(f"sqlite:///bank.db")
    Base.metadata.create_all(engine)

    Session = sessionmaker()            # factory for sessions: create Session class
    Session.configure(bind=engine)      # bind session to the engine

    BankGUI()
