"""Importing logging and beautifultable package"""
import logging
from beautifultable import BeautifulTable

# creating log file loans.log and storing logs into it
logging.basicConfig(
    filename="loans.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
)


class LoanScheduler:
    """
    This class consist of calculate_loan method which will
    schedule the loan payments according to year
    and customer will have to pay that number of
    payments
    """

    def __init__(self, loan_amount, rate, payment_years):
        """
        This will initialize the class variables and
        create the table schema.
        """
        logging.info("START EXECUTING __init__ METHOD")

        # intializing class variables
        self.loan_amount = loan_amount
        self.rate = rate
        self.payment_years = payment_years

        # createing table and schema of table with column names
        self.table = BeautifulTable()
        self.table.columns.header = [
            "MONTH",
            "LOAN AMOUNT",
            "PAYMENT",
            "INTEREST",
            "PRINCIPLE",
            "NEW LOAN AMOUNT",
        ]

        logging.info("__init__ METHOD EXECUTED")

    def calculate_loan(self):
        """
        This function will schedule the loan amount in number of payments customers have to pay.
        """
        try:
            logging.info("START EXECUTING calculate_loan METHOD")

            # calculating interest rate, total number of payments
            # and calculating payment amount
            sr_no = 0
            interest_rate = self.rate / 12.0
            total_payments = self.payment_years * 12
            payment = (interest_rate * self.loan_amount) / (
                1 - ((1 + interest_rate) ** (-total_payments))
            )

            # calculating princile, interest and amount payable in each month
            # appending each month record into table
            while self.loan_amount > 0:
                sr_no += 1
                interest = self.loan_amount * interest_rate
                principle = payment - interest

                if self.loan_amount - payment < 0:
                    principle = self.loan_amount

                self.table.rows.append(
                    [
                        sr_no,
                        self.loan_amount,
                        payment,
                        interest,
                        principle,
                        self.loan_amount - principle,
                    ]
                )

                self.loan_amount = self.loan_amount - principle

            logging.info("calculate_loan METHOD EXECUTED")

        except Exception as exc:  # pylint: disable=broad-except
            logging.exception(
                "Some exception has occurred..!! Exception is: %s", exc
            )

    def display(self):
        """This function will display the table with total payments information"""
        print(self.table)
        logging.info("display METHOD EXECUTED")


try:
    logging.info("Program Start Executing...")

    # taking user input
    LOAN_AMOUNT = int(input("Enter the loan amount: "))
    RATE = float(input("Enter the rate: "))
    PAYMENT_YEARS = float(input("Enter the payment years: "))

    # checking for null or negative values
    if LOAN_AMOUNT <= 0 or RATE <= 0 or PAYMENT_YEARS <= 0:
        print("Any argument can not be 0.")
    else:
        OBJ = LoanScheduler(LOAN_AMOUNT, RATE, PAYMENT_YEARS)
        OBJ.calculate_loan()
        OBJ.display()

    logging.info("Program Executed Successfully...!!")

except Exception as exc:  # pylint: disable=broad-except
    logging.exception("Some exception has occurred..!! Exception is: %s", exc)
