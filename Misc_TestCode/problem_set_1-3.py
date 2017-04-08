"""
Description :
A program to calculate the credit card balance after one year if a person only pays the minimum monthly payment
required by the credit card company each month.

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal

Monthly interest rate= (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

 """
balance = 320000
annualInterestRate = 0.2


monthly_interest_rate = annualInterestRate/12
lower_fixed = balance/12
upper_fixed = balance * (1 + monthly_interest_rate)**12 / 12.0
fixed = 0
unpaid_balance = 0
balance_copy = balance

while True:
    balance_copy = balance
    fixed = (lower_fixed+upper_fixed)/2
    for i in range(12):
        # min_monthly_payment = monthlyPaymentRate * balance
        unpaid_balance = balance_copy - fixed
        balance_copy = unpaid_balance + monthly_interest_rate * unpaid_balance
    if balance_copy > 0.01: lower_fixed = fixed
    elif balance_copy < 0: upper_fixed = fixed
    else: break


print round(fixed,2)