#1)Write a program to reverse a string.
c=input("Enter your input: ")
c=c[::-1]
print(c)
#2)Write a function that accepts a string and prints the number of uppercase letters and lowercase letters.
def fun():
    d = input("Enter your input : ")
    u = 0
    p = 0
    for i in d:
        if i == i.lower():
            u += 1
        else:
            p += 1
    print(f"NO.lower case charecter:{u}")
    print(f"NO.upper case charecter: {p}")
fun()
#3)Create a function that takes a list and returns a new list with unique elements of the first list.
def uni(list):
    d=[]
    print(f"list -input: {list}")
    for i in list:
        if list.count(i)>1:
            pass
        else:
            d.append(i)
    print(f"output-list:{d}")
uni([1,2,3,1,4,5,4,6])
#4) Write a program that accepts a hyphen-separated sequence of words as input and prints the words
#in a hyphen-separated sequence after sorting them alphabetically.
def sep():
    d=input("enter your input: ")
    f=d.split('-')
    o=""
    print(f"input entered without hiphen in a list form:{f}")
    f.sort()
    for i in f:
        print(i)
#calling function sep
sep()
#5. Write a program that accepts a sequence of lines as input and prints the lines after making all
#characters in the sentence capitalized.
#Sample input: Hello world Practice makes man perfect
#Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT
def cap():
    inp=input("enter your input: ")
    print(inp.upper())
cap()
#6. Define a function that can receive two integral numbers in string form and compute their sum and
#print it in the console.

def sum():
    a=int(input("enter first number: "))
    b=int(input("enter second number: "))
    c=a+b
    print(f"Sum: {c}")
sum()
#7. Define a function that can accept two strings as input and print the string with the maximum length
#in the console. If two strings have the same length, then the function should print both the strings line
#by line.
def string():
    a=input("Enter first string :")
    b=input("Enter second string: ")
    l1=len(a)
    l2=len(b)
    if l1>l2:
        print(a)
    elif l2>l1:
        print(b)
    else:
        print(a)
        print(b)
string()
#8. Define a function which can generate and print a tuple where the values are square of numbers
#between 1 and 20 (both 1 and 20 included).
def tup():
    for i in range(1,21):
        s=i*i
        result=tuple([i,s])
        print(result)
tup()
#9. Write a function called showNumbers that takes a parameter called limit. It should print all the
#numbers between 0 and limit with a label to identify the even and odd numbers.
def ShowNumbers(limit):
    for i in range(0,(limit+1)):
        if i%2==0:
            print(f"{i} EVEN")
        else:
            print(f"{i} ODD")

ShowNumbers(6)
#10)Write a program which uses filter() to make a list whose elements are even numbers between 1
#and 20 (both included)
def filtereven(num):
    if num % 2 == 0:
        return True
    else:
        pass
list1=list(range(21))
filtered=filter(filtereven,list1)
print(list(filtered))

#11)Write a program which uses map() and filter() to make a list whose elements are squares of even
#numbers in [1,2,3,4,5,6,7,8,9,10].

list1=[1,2,3,4,5,6,7,8,9,10]
filtereven=list(filter(lambda n:n%2==0,list1))
print(f"List of even numbers: {filtereven}")
doubleeven=list(map(lambda n:n*2,filtereven))
print(f"list of double of even numbers:{doubleeven}")

#12. Write a function to compute 5/0 and use try/except to catch the exceptions
def div(a,b):
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print("Please enter valid number,", e)
div(3,0)
#13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
import functools
l=[1,2,3,4,5,6,7]
print (functools.reduce(lambda a,b :str(a)+str(b) ,l))

#14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
#Make sure to use only higher order functions.

x=list(range(20))
print(x)
y=list(filter(lambda x : x%3!=0 and x%7==0,x))
print(y)

#15. Write a program in Python to multiply the elements of a list by itself using a traditional function
#and pass the function to map() to complete the operation.

l=[1,2,3,4]

def func1(n):
    return n*n
result=list(map(func1 ,l))
print(result)
#16. What is the output of the following codes:
#1)2
#2) name error for f ,as it is not defined anywhere.
#after
#after f?
