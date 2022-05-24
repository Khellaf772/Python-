

# Programming Assignment 9: Palindrome Program in CS 110A:
# A program that checks if a string is a palindrome or not.
# Written by __________(Khellaf)_________
###################################################

import math

def checking():
  ''' 
  It asks a user to enter a word or a phrase, and then it checks what characters 
  that word or phrase has. It keeps only the alphabet characters. Next, it will find 
  the middle of that word or phrase in order to compare the characters of the 1st position
  and the last position and so on if they are equal, so it prints a palindrome; otherwise,
  it is not a palindrome.

  '''

  text = input(str("Please enter a word or phrase: ")).lower()
  new_text = ""     #new_text will be free of punctuations and spaces if there are any. 
  value = False
  
  for char in text:
    if char.isalpha():
      new_text += char
          
  print("The reversed phrase is:",new_text[::-1]) #To know what the word or the phrase would be in reversed way.
                                                    
  L = len(new_text)
  middle = math.floor(L/2) # floor to get the smallest value

  for i in range(0, middle):
    if new_text[i] != new_text[L-1-i]:
      value = True
      
  if value == True:
    print("The text you entered: '" + text + "' is not a palindrome.")
  else:
    print("The text you entered: '" + text + "' is a palindrome.")
 

def YES_NO():
  '''
  After the user entered a word or phrase, he/she will be asked if he/she 
  want to check another word or phrase. If yes/y or no/n entered as answers,
  the program will allow another attempt and if the answers different than 
  yes/y or no/n, a message will be displayed and explain for the user that 
  yes/y or no/n must be the answers because it is a YES/NO question.

  ''' 

  condition = 0
  while condition == 0:
    ask = input("Do you want to enter another word? ").lower()
    print()
    if ask == "yes" or ask == "y":
      checking()
    elif ask == "no" or ask == "n":
      print(end='')
      condition = 1
    else:
      print("It is a yes or no question! You must enter yes/y or no/n. Try again.")
            
def main():
  '''
  It calls the functions in order the code will run
  '''

  checking()
  YES_NO()
 

main()
