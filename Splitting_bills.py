


# Objective: To write a program to splits bills.
# Written by Khellaf

def main():
    people = int(input("How many people are needed to share the bills? "))
    peopleNum = getPositiveNum(people)

    nameList = []
    paidList =[]
    for i in range(1,peopleNum+1):
       name = str(input("What is name of person "+str(i)+"? "))
       nameList.append(name)
    print()   
    #print(nameList)

    aver = getAverage(nameList,peopleNum,paidList)
    finalpay(paidList,aver,nameList)

def getPositiveNum(peopleLL):
    while peopleLL <= 0:
      peopleLL = int(input("Please inter a positive number.\nHow many people are needed to share the bills? "))
    return peopleLL

def getAverage(nList,peoples,Alist):
    total = 0
    for i in nList:
       #paid = float(input(i+ " paid how much? $"))
       paid = float(input("How much did "+i+" pay? $"))
       total = total + paid
       Alist.append(float(paid))
    average = total / peoples
    print("The average amount per person is",format(average,'.2f'))
    return average
    #print(paidList)

def finalpay(paidList,aver,listOfName):
    paymentList = []
    for i in paidList:
        finalAmount = aver - i
        paymentList.append(float(format(finalAmount,",.2f")))
    print()
    print("After subtracting the amount each person had paid, they need to pay the following:")

    for A in range(len(listOfName)):
        #for amount in paymentList:
          if paymentList[A] == 0:
             print(listOfName[A]," doesn't need to pay anything.")
          elif paymentList[A] < 0:
             c_n_t_p = abs(paymentList[A])
             print(listOfName[A],"needs to be refunded $"+str(c_n_t_p))
          else:
             print(listOfName[A],"needs to pay $"+str(paymentList[A])+" extra.")

main()
