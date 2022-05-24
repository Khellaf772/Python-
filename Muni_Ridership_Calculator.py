

# Programming Assignment 2: Muni Ridership Calculator
# A program to ask the user which Muni line was surveyed,
# then asks the user how many days the survey was conducted 
# and asks the number of riders that were counted.
# Finally the program divides the number of riders by the number of days and outputs the resulting average daily ridership.
#       Written by __________(Khellaf)_________
###################################################

print("Welcome to the Muni Ridership Calculator.")

line = input("Which Muni line did you survey? " )
days = int(input("How many days did you survey it? " ))
riders = int(input("How many riders did you count? " ))

Average = (riders / days)
print("According to your survey, an average of",Average,"people rode the",line, "per day.")
