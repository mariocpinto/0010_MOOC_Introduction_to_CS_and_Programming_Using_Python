## PROBLEM 1: PAYING THE MINIMUM
#
#Write a program to calculate the credit card balance after one year
#if a person only pays the minimum monthly payment required by the 
#credit card company each month.
#
#The following variables contain values as described below:
#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal
#monthlyPaymentRate - minimum monthly payment rate as a decimal
#
#For each month, calculate statements on the monthly payment 
#and remaining balance, and print to screen something of the format:
#
#Month: 1
#Minimum monthly payment: 96.0
#Remaining balance: 4784.0
#
#Finally, print out the total amount paid that year 
#and the remaining balance at the end of the year in the format:
#
#Total paid: 96.0
#Remaining balance: 4784.0
#A summary of the required math is found below:
#
#Monthly interest rate= (Annual interest rate) / 12.0
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month = (Monthly unpaid balance) + 
#                                (Monthly interest rate x Monthly unpaid balance)

# SampleInput
#balance = 4213
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04

no_of_mths = 12
total_due = balance
total_paid = 0

for month in range(1,no_of_mths+1):
    
    min_monthly_pmt = monthlyPaymentRate*total_due
    total_paid += min_monthly_pmt
    unpaid_bal = total_due - min_monthly_pmt
    total_due = unpaid_bal*(1 + annualInterestRate/12)
    
    print 'Month:', month
    print 'Minimum monthly payment:', round(min_monthly_pmt,2)
    print 'Remaining balance:', round(total_due,2)
    
print 'Total paid:', round(total_paid,2)
print 'Remaining balance:', round(total_due,2)
    
    
    
    
    
    