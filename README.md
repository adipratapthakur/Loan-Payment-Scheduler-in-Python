# Loan-Payment-Scheduler-in-Python
  
Question:- Write a program to create Loan Payment Schedule  
  
•	Interest is the rate you pay towards the loan, here it will be used as a decimal  
•	(so for example: 5% is .05).  
•	The number of payments will be determined by how many years the loan is for multiplied by 12 (one payment per month).  
•	If your loan is for less than a year, you can use a fraction (i.e. 9 months is .75)  
•	Interest can be calculated by multiplying the interest rate and the current loan value  
•	Each month this number will be different, so we include it in the loop.  
•	Principle is the actual amount of the payment that goes towards the loan balance and is found by subtracting the calculated interest from the payment  
•	Our loop condition states that we are going to loop as long as the value of the loan is greater than 0.  
•	The easiest check here is to see whether the next payment will cause the loan to be less than 0, and if so, then the principle payment of this month will be equal to the loan value.  
•	Finally, the loan value is updated by subtracting the current months principle payment.  
•	Compute the loan payment schedule over the lifetime of the loan using BeautifulTable  
•	`pip install beautifultable` (https://pypi.org/project/beautifultable/)  
  
1. Installing the beautifultable package  
  
`pip install beautifultable`  
  
2. Run the Python Module `loan_payment_scheduler.py`  
  

  
