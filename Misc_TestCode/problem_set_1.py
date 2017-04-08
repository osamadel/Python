"""
Description :
A program to calculate the credit card balance after one year if a person only pays the minimum monthly payment
required by the credit card company each month.

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

 """
balance = 3926
annualInterestRate = 0.2
# monthlyPaymentRate = 0.02
# For every month there is
# min_monthly_payment = 0

monthly_interest_rate = annualInterestRate/12
fixed_monthly_payment = 0
unpaid_balance = 0
balance_copy = balance

while balance_copy > 0:
    balance_copy = balance
    fixed_monthly_payment += 10
    for i in range(12):
        # min_monthly_payment = monthlyPaymentRate * balance
        unpaid_balance = balance_copy - fixed_monthly_payment
        balance_copy = unpaid_balance + monthly_interest_rate * unpaid_balance


print round(fixed_monthly_payment,2)