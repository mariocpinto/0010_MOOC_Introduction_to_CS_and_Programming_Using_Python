#PROBLEM 3: USING BISECTION SEARCH TO MAKE THE PROGRAM FASTER (25 points possible)
#
#The following variables contain values as described below:
#
#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal
#
#To recap the problem: 
#we are searching for the smallest monthly payment such that we can pay off
#the entire balance within a year. What is a reasonable lower bound for this payment value? 
#$0 is the obvious anwer, but you can do better than that. 
#If there was no interest, 
#the debt can be paid off by monthly payments of one-twelfth of the original balance,
#so we must pay at least this much every month. 
#One-twelfth of the original balance is a good lower bound.
#
#What is a good upper bound? 
#Imagine that instead of paying monthly, we paid off the entire balance at the end of the year. 
#What we ultimately pay must be greater than what we would've paid in monthly installments, 
#because the interest was compounded on the balance we didn't pay off each month. 
#So a good upper bound for the monthly payment would be one-twelfth of the balance, 
#after having its interest compounded monthly for an entire year.
#
#In short:
#
#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly payment lower bound = Balance / 12
#Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

# SampleInput
#balance = 320000
#annualInterestRate = 0.2

lower_bound = balance/12.0
upper_bound = (balance*(1 + annualInterestRate/12)**12)/12.0
epsilon = .01

no_of_mths = 12
total_due = balance
min_monthly_pmt = 0

iter_no = 0
max_iter = 200

while ( ((upper_bound - lower_bound) > epsilon) and iter_no < max_iter ):

    iter_no += 1

    min_monthly_pmt = 0.5*(lower_bound + upper_bound)   
    #print round(lower_bound,2), round(min_monthly_pmt,2), round(upper_bound,2)
      
    total_due = balance

    for month in range(1,no_of_mths+1):
    
        unpaid_bal = total_due - min_monthly_pmt
        total_due = unpaid_bal*(1 + annualInterestRate/12)

    if total_due > 0:
        lower_bound = min_monthly_pmt
    else:
        upper_bound = min_monthly_pmt
        
print 'Lowest Payment:', round(min_monthly_pmt,2)
    