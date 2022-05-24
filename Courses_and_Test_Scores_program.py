

# Programming Assignment 11: Courses and Test Scores in CS 110A:
# A program that uses a 2-dimensional list to store 
# all the test scores in all of a student's classes.
# Written by __________(Khellaf)_________
###################################################

def Averagelist(List):
  '''
  A function that calculate the average score for 
  every course and store them in a list.
  '''

  AvList = []

  for item in List:
    total = 0
    average = 0
    for j in item:
      total += j 
      average = total / len(item)
    AvList.append(float(average))

  AverageScore(AvList)   
 

def AverageScore(AvList):
  '''
  A function that prints the average score for every 
  course and the highest score using a list (AvList).  
  '''
  print()
  for element in range(1,len(AvList)+1):
    print("The average score for course " +str(element)+ " is ",AvList[element-1])

  AvList.sort()
  Hscore = AvList[len(AvList)-1]
  print() 
  print("The highest average score is", Hscore)
 
      
def main():
  
  List = []
  total = 0   

  courses = int(input("How many courses are you taking? "))
  if courses > 0:
    for i in range(1, courses+1):
      Test = []
      print()
      tests = int(input("How many tests are in course number {}:? ".format(i)))
      if tests >= 0:
        for y in range(1,tests+1):
          score = float(input("What was your score on test " +str(y)+ " for course " + str(i)+"? "))
          Test.append(score)
      elif tests < 0:
        print("Invalid number of tests!")
            
      List.append(Test)
    Averagelist(List)
  elif courses == 0:
    print("Okay! You have no courses. Good Luck!") 
  elif courses < 0:
    print("You must enter a real number of courses!")
  
  


main()
