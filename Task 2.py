#(1).Write a program in Python to perform the following operation:
#If a number is divisible by 3 it should print “Consultadd” as a string
#If a number is divisible by 5 it should print “Python Training” as a string
#If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
#string.

a=int(input("enter a number: "))
if a%3==0 and a%5==0:
    print("Consult add Python Training.")
elif a %3==0:
    print("Consult add")
elif a%5==0:
    print("Python Training")
else:
    print("not divisible by 3 or 5")
#2. Write a program in Python to perform the following operator based task:
#Ask user to choose the following option first:
#If User Enter 1 - Addition
#If User Enter 2 - Subtraction
#If User Enter 3 - Division
#If User Enter 4 - Multiplication
#If User Enter 5 - Average
#Ask user to enter two numbers and keep those numbers in variables num1 and num2
#respectively for the first 4 options mentioned above.
#Ask the user to enter two more numbers as first and second for calculating the average as
#soon as the user chooses an option 5.
#At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
#NOTE: At a time a user can only perform one action

print("addiion: 1"'\n'"subtaction : 2 "'\n'"Division: 3"'\n'"Multiplication:4"'\n'"Average:5")
i=int(input("Select the appropriate number to perform desired operation: "))
if i==1:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number: "))
    result=num1+num2
    print(f"your result is {result}")
elif i==2:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number: "))
    result = num1 - num2
    if result<0:
        print("Negative")
    else:
        print(f"your result is {result}")

elif i==3:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number: "))
    result = num1/num2
    print(f"your result is {result}")
elif i==4:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number: "))
    result = num1 * num2
    print(f"your result is {result}")
else:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter first number:"))
    num4 = int(input("Enter second number: "))
    sum=(num1+num2+num3+num4)
    result=sum/4
    print(result)
#(3)write proggram in python to implement the given flow chart

a=10
b=20
c=30
avg=((a+b+c)/3)
print(f" avg= {avg}")
if avg > a and avg >b and avg >c:
    print("Average is higher than a,b,c")
else:
    if avg > a and avg > b:
        print("avg is higher than a,b,c")
    else:
        if avg >a and avg >c:
            print("avg is higher than a,c")
        else:
            if avg >b and avg>c:
                print("avg is higher than b,c")
            else:
                if avg > a:
                    print("avg is just higher than a")
                elif avg > b:
                    print("avg is just higher than b ")
                elif avg>c :
                    print("avg is just higher than c")
#Write a program in oython to break and continue if following case occurs
#if user enter -ve number then break the loop and print "It's going" or else print " Good Going"
for i in range(10):
    j=int(input("Enter a number: "))
    if j<0:
        break
    else:
        print("Good Going")
print("it's over")
# A program in python which will find all such numbers which are divisible by 7 and not a multiple of 5

for i in range(2000,3201):
    if i%7 ==0 and i%5!=0:
        print (i)
#out put of the code?
#1-answer)
#will get a type error as int object is not interable
#2)answer)
# 0,error
#1,error
#2

#3-Answer)
# 0
# 1
# 2
# 3
# 4
#--------------------------------------------------
#7)Write a program that prints all numbers from 0 to 6 except 3 and 6

for i in range(0,7):
    if i!=3 and i!=6:
        print(i)
    else:
        continue

#write a program that accepts string as an input from user and calculate number of digits and letters
x=input("enter some input: ")
x=x.lower()
p=[]
b=["0","1","2","3","4","5","6","7","8","9"]
c=[]
d=[]
for i in x:
    if i in b:
        c.append(i)
    else:
        if i==" ":
            q=[]
            q.append(i)
        else:
            d.append(i)
l1=len(c)
l2=len(d)
print(f"number of letters: {l2}")
print(f"Number of digits: {l1}")
#9)guess game part-a
from random import seed
from random import randint
while True:
    X= randint(0,1000)
    y=int(input("Enter your guess: "))
    if y==X:
        print("You won!!")
        break
# guess game part-b
from random import seed
from random import randint
while True:
    X= randint(0,1000)

    y=int(input("Enter your guess: "))
    answer = input("press yes to continue and no to stop game")
    answer.lower()
    if y==X or answer=="no":
        if y==X:
            print("You won!!")
            break
        elif answer=="no":
            break
#Enter a program that guess 5 time a lucky number part a
from random import randint
x = randint(0, 500)
counter = 1

while counter <= 5:
    y = input("enter your guess: ")
    if y == x:
        print("Good guess!")
    else:
        if counter != 5:
            print("Try again!")
    counter = counter + 1
print("Game over!")

#11-part b with break statement and statement "Sorry but that was not very successful" after 5th try

from random import randint
x = randint(0, 500)
counter = 1

while counter <= 5:
    y = input("enter your guess: ")
    if y == x:
        print("Good guess!")
        break
    else:
        if counter != 5:
            print("Try again!")
        else:
            print("Sorry but that was not very successful")
            print("Game over!")

    counter = counter + 1




