#1)Write a program in Python to allow the error of syntax to be handled using exception handling.
def fub():
    try:
        print("hello"
    except SyntaxError as error:
        print("you have syntax error, ", error)
    finally:
        print("hey")
fub()
#2)Write a program in Python to allow the user to open a file by using the argv module. If the
#entered name is incorrect throw an exception and ask them to enter the name again. Make sure
#to use read only mode.
import sys
file=input("enter file name: ")
try:
    with open (sys.argv,"r") as filename:
        cont=filename.read()
        print(cont)

except:
    print("file not found!!")
finally:
    print("thank you!!")

#3. Write a program to handle an error if the user entered a number more than four digits it should return “The length is too short/long !!! Please provide only four digits”
num=input("enter your number: ")
d = len(num)
if d <= 4:
    print("hello")
else:
    raise Exception("The length is too short/long !!! Please provide only four digits")
#Create a login page backend to ask users to enter the username and password. Make sure to
#ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
#should not be more than 3 times.
name="Naima"
password="Poocha123"
n = input("Enter your username: ")
if n==name:
    for i in range(3):

        p = input("enter your pass word: ")
        r = input("Re-enter your pass word: ")
        if p == r or p!=r:
            if p != password  or p!=r:
                print("Your have entered wrong password")

            else:
                print(f"Welcome {name}, you have logged in")
                break
else:
    raise Exception("Please check the credential you have entered!!")
#6. Read doc.txt file using Python File handling concept and return only the even length string from the file.

f=open("doc.txt","r")
p=f.readlines()
for i in p:
    if len(i)%2==0:
        print(i)
    else:
        print(f"this is not having length of even numbers:{i}")













