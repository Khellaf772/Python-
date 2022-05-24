# Programming Assignment 7: Rock-Paper-Scissors Program in CS 110A:
# A program to play the rock-paper-scissors game using two functions
# and if statements .
# Written by __________(Khellaf)_________
###################################################

import random

def Lets_Play(List, move):
  '''
  Lets_Play() is the function that runs the user's and computer's move
  ''' 
  # here we start from the user's move, and the program outputs the user as a winner.   
  if List == "Paper" and (move.lower() == "scissors" or move.lower() == "scissor"): 
    print("You Win! Scissors Cut Paper!!")
  elif List == "Rock" and (move.lower() == "paper"):
    print("You Win! Paper covers Rock!!") 
  elif List == "Scissors" and (move.lower() == "rock"): 
    print("You Win! Rocks break Scissors!!")   
  # here where the computer's move begins, and the program outputs the computer as a winner. 
  elif move.lower() == "paper" and List == "Scissors":
    print("Computer Wins! Scissors Cut Paper!!")
  elif move.lower() == "rock" and List == "Paper":
    print("Computer Wins! Paper covers Rock!!")  
  elif (move.lower() == "scissors" or move.lower() == "scissor")  and List == "Rock":
    print("Computer Wins! Rocks break Scissors!!")
  # here where both moves are equal and the program outputs "tie with 'comp's or user's move'"
  elif (move.lower() == "scissors" or move.lower() == "scissor") and List == "Scissors":
    print("Tie with Scissors!") 
  elif move.lower() == "paper" and List == "Paper":
    print("Tie with Paper!")
  elif move.lower() == "rock" and List == "Rock":
    print("Tie with Rock!")
  # here if the user inputs a wrong move, the program outputs "Oops!! Invalid move"
  else:
    print() #I added print() to separte the user and computer outputs from invalid message and make it clearer for the user.
    print("Oops!! invalid move")  
    print("Please check your spelling and try again.")
 
def main():
  '''
  in this function, the user will be asked to enter his move
  and the computer will make his random move as automatically.
  so the only whom will be asked is the used. 
  '''
  print("Hello, Welcome to the Rock-Paper-Scissors Game ")
  print("BEFORE YOU START, PLEASE CHECK YOUR SPELLING")
  print()  # I added print here to separate the headings from the outputs

  ComputerMove= ["Paper", "Rock" ,"Scissors"]
  List = random.choice(ComputerMove) 
  move = input("please enter your move among Paper, Rock, or Scissors: ")
  print("Computer's move is",List)
 
  Lets_Play(List, move)
  
    
main()
    
