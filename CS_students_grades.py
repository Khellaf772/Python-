

# Programming Assignment 14: Writing Functions in CS 110A:
# A program that checks scores of exercises and assignments 
# in order to find a proximate grade for CS 110A students.
# Written by __________(Khellaf)_________
###################################################


def main():

  print("This program will find proximate grades for CS 110A students")
  print("             ***************             ")
  print()
  chapters = int(input("How many chapters have you studied so far? "))
  exolist = []
  assgnlist = []

  if chapters != 0:
    print("How many graded exercises and assignments there were in every chapter? ")
    exercises = int(input("Number of exercises: "))
    assignments = int(input("Number of assignments: "))
    if exercises == 0 and assignments == 0:
      print("Okay, no exercises or assignments.")
      return
    else:       
      print()
    ExoInChapters(chapters, exolist, exercises)
    AssgnInChapters(chapters, assgnlist, assignments)
    gradesfun(assignments, exercises, chapters, exolist, assgnlist)
  else:
    print("Okay then! No grades availble.")

def ExoInChapters(Chap, alist, exo):
  '''
  It gives to the student the total credits he/she got in all exercises either with or without extra points. 
  '''    
  print("The maximum number of credits for each exercise in every chapter is 10,")   
  ask = input("Exluding tests, did you receive other credits greater or less than 10? (yes/no) ")
  if ask[0].lower() == "y":
    othercredits = print("What were these other credits? ")
    condition = True
    while condition:
      score = (input("Enter the score and hit 'q' if you are done: "))
      if not score.isalpha():
        alist.append(float(score))
        condition
      else:
        condition = False
    if sum(alist) > (len(alist) *10):
      print("Nice! You got",sum(alist)-(len(alist) *10)," extra credits in all the exercises you had in addition to",Chap*exo*10)
    elif sum(alist) < (len(alist) *10) and sum(alist) != 0:
      print("You didn't have extra credits, and you got only",(Chap*exo*10)-sum(alist),"out of",Chap*exo*10)      
    elif sum(alist) == 0:
      print("You didn't have extra credits, and you got",(Chap*exo*10)-(len(alist)*10),"out of",Chap*exo*10)
    elif sum(alist) == (len(alist)*10):
      print("You didn't have extra credits, and you got",(Chap*exo*10),"out of",Chap*exo*10)
  elif ask[0].lower() =="n":
    print("Great! You must have received full (10) points for every exercise in all "+str(Chap)+" chapters.")
  print()


def AssgnInChapters(Chap, blist, assgn):
  '''
  It gives to the student the total credits he/she got in all assignments either with or without extra points. 
  '''
  print("The maximum number of credits for each assignment in every chapter is 45,")
  askagain = input("Exluding tests, did you receive credits greater or less than 45? (yes/no) ")
  if askagain[0].lower() == "y":
    othercredits = print("What were these credits? ")
    condition = True
    while condition:
      score = (input("Enter the score and hit 'q' if you are done: "))
      if not score.isalpha():
        blist.append(float(score))
        condition     
      else:
        condition = False
    if sum(blist) > (len(blist) *45):    
      print("Nice! You got",sum(blist)-(len(blist) *45)," extra credits in all the assignments you had in addition to",Chap*assgn*45)
    elif sum(blist) < (len(blist) *45) and sum(blist) != 0:
      print("You didn't have extra credits, and you got only",(Chap*assgn*45)-sum(blist),"out of",Chap*assgn*45)  
    elif sum(blist) == 0 :
      print("You didn't have extra credits, and you got",(Chap*assgn*45)-(len(blist)*45),"out of",Chap*assgn*45)
    elif sum(blist) == (len(blist)*45):
      print("You didn't have extra credits, and you got",(Chap*assgn*45),"out of",Chap*assgn*45)         
  elif askagain[0].lower() == "n":
    print("Great! You must have received full (45) points for every assignment in all "+str(Chap)+" chapters.")
 

def ExercisesScore(Alist, chap, exo):
  '''
  It calculates the sum of the exercises' scores entered other than 10 (10 is the
  maximum number of points a student can get without extra credits) and returns that sum.
  '''
  sumlist = 0
  for i in Alist:
    sumlist += i
  scoresum = sumlist + ((chap * exo * 10) - (len(Alist) * 10))  
  return scoresum


def AssignmentsScore(Blist, chap, assgn):
  '''
  It calculates the sum of the assignments' scores entered other than 45 (45 is the
  maximum number of points a student can get without extra credits) and returns that sum.
  '''
  sumlist = 0
  for item in Blist:
    sumlist += item
  assgnscore = sumlist + ((chap * assgn * 45) - (len(Blist) * 45))
  return assgnscore 


def gradesfun(assignments, exercises, chapters, exolist, assgnlist):
  '''
  It gives the student what grade he/she might 
  get after checking all the scores given
  '''

  s1 = ExercisesScore(exolist, chapters, exercises)
  s2 = AssignmentsScore(assgnlist, chapters, assignments)

  expectedAssgPoints = 45 * assignments * chapters
  expectedExoPoints = 10 * exercises * chapters
  alltogether = expectedAssgPoints + expectedExoPoints
  actualscore = ((s1 + s2)/alltogether)*100

  print()
  if actualscore > 100:
    print("You must have an A with a higher percentage of",format(actualscore, ",.2f"),"% than expected.")
  elif 90 <= actualscore <= 100:
    print("Excellent, you got an A with a score of",format(actualscore,",.2f"),"%.")  
  elif 80 <= actualscore <= 90:
    print("Nice, you got a score of",format(actualscore, ",.2f"),"% which is a B.")
  elif 80 <= actualscore <= 90:    
    print("Acceptable, a passable score of",format(actualscore, ",.2f"),"%. Well done.")
  elif 70 <= actualscore <= 80:
    print("Well, you got a score of",format(actualscore, ",.2f"),"% which means a C.")
  elif 65 <= actualscore <= 70:
    print("Oops you got a D!, this is not funny. You must have worked hard because your score of",format(actualscore, ",.2f"),"% is so low ")
  elif actualscore <= 65:
    print("I think will fail with a score of",format(actualscore, ",.2f"),"% which is an F")     

         
main()
