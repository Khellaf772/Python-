

#Assignment 8: Consumer Loan Program in CS 110A:
# A program that calculates how long it will take to pay off a loan using three functions
# Written by __________(Khellaf Amara)_________
###################################################

import math

def calculation(balance, int_rate, m_payment):
  '''
  A function that makes calculation of interests and balances based on the user inputs
  and outputs advice for the user if the inputs are not satisfying.
  '''

  interest = (int_rate/12) / 100
  current_rate = balance * interest
  new_balance = balance 
  Total_interest = 0
  if current_rate > m_payment:
    print("You must make payments of at least ${:,.2f}".format(current_rate + 1))
    print("Because your monthly interest is ${:,.2f}".format(current_rate))
    print("** Don't get overwhelmed with debt! **")  
  else: 
     
    while new_balance > 0: 
      new_rate = new_balance * interest 
      new_balance += new_rate - m_payment
      Total_interest += new_rate     
    months(new_balance, m_payment, balance, Total_interest) 

    
def months(new_balance, m_payment, balance, Total_interest):
  ''' 
  A function that calculates the number of months based on 
  the amount borrowed, interests and the monthly payment
  '''

  months = math.ceil((balance + Total_interest)/ m_payment)
  final_payment = m_payment - (-new_balance)
  print("Your debt will be paid off after", months ,"months, with a final payment of just ${:,.2f}".format(final_payment))
  print("The total amount of interest you will pay during that time is ${:,.2f}".format(Total_interest))
  print("** Don't get overwhelmed with debt! **") 
     
    
def main():
  '''
  A function that asks the user for positive inputs and if the
  inputs are negative, it asks another time for positive inputs.
  '''

  print("** Welcome to the Consumer Loan Calculator **")
  balance = float(input("How much do you want to borrow? $"))
  while balance <= 0:
    print("You must enter a positive number!")
    balance = float(input("How much do you want to borrow? $"))
  int_rate = float(input("What is the annual interest rate expressed as a percent? "))
  while int_rate <= 0:
    print("You must enter a positive number!")
    int_rate = float(input("What is the annual interest rate expressed as a percent? "))
  m_payment = float(input("What is the monthly payment amount? $"))
  while m_payment <= 0:
    print("You must enter a positive number!")
    m_payment = float(input("What is the monthly payment amount? $"))

  calculation(balance, int_rate, m_payment)


main()
