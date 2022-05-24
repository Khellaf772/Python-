

# Programming Assignment 5: Rolling Dice in, CS 110A:
# This program simulates the rolling of dice in a game like Dungeons and Dragons. 
# it asks the user how many players are playing, how many dice they are each rolling, 
# and how many sides are on each die by using one function and two for loops.
# Written by __________(Khellaf)_________
###################################################


import random 

Players = int(input("How many players are rolling dice? "))
dice = int(input("How many dice does each player roll? "))
dice_Sides = int(input("How many sides does each die have? "))


 
def diCe():
  '''
  in this function, we called the random function in order to output
  random numbers that are on each side of a die/dice played by the user
  and then, it calculates the sum of these random numbers which is returned
  at the end.  
  '''

  Total = 0   #initializing the sum

  for a in range(1,dice+1):
     NumOnSides = random.randrange(1,dice_Sides+1)     
     print(NumOnSides)
     Total += NumOnSides          # here where the sum is calculated.
  print("That totals:",Total)
  return Total

''' 
for loop outputs number of each player(#1, #2, #3...), and here diCe()
is called to be executed in this loop.
'''

for i in range(1, Players+1):        
  print()                    # I added print() in order to make a space between 
                             # the previous round and the coming round, also to make it
                             # clearer for the reader to understand. 
  print("Player " +str(i)+ " rolled:")
  diCe()
