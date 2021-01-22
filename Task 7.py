#1. Write a program that calculates and prints the value according to the given formula:
#Q= Square root of [(2*C*D)/H]
import math
H=30
C=50
q=2*C/H
print("enter your list,where elements are separated by space.")
l=[int(x) for x in input().split()]
print(f"list you have entered:{l}")
r=[]
for i in l:
    u=i*q
    y=math.sqrt(u)
    r.append(y)
print(r)
#Define a class named Shape and its subclass Square. The Square class has an init function which
#takes length as argument. Both classes have an area function which can print the area of the shape
#where Shape’s area is 0 by default.
class shape:
    def __init__(self,n,l):
        print("this is super class named shape")
        self.n=n
        self.l=l

    def area(self):
        if self.n==0:
            print("area=0")
        elif self.n==4:
            area=(self.l*self.l)
            print(f"area: {area}")
class square(shape):
    def __init__(self,l,n):
        shape.__init__(self,l,n)
        self.n=n
        print("this is square")

x=square(5,4)
x.area()
#Create a class to find three elements that sum to zero from a set of n real numbers
#Input array: [-25,-10,-7,-3,2,4,8,10]
#Expected output: [[-10,2,8],[-7,-3,10]]
l=[-25,-10,-7,-3,2,4,8,10]
class find:
    def __init__(self,l):
        self.l=l
        self.li=[]
        self.l2=[]
        self.l3=[]
    def zero(self):
        for i in self.l:
            c=i
            for j in self.l:
                k=j
                for s in self.l:
                    h=s
                    if c+k+h==0:
                        if c and k and h not in self.l2:
                            self.l2.append(c)
                            self.l2.append(k)
                            self.l2.append(h)
                        else:
                            pass
                    else:
                        pass

        print(self.l2)
test=find(l)
test.zero()
#Create a Time class and initialize it with hours and minutes.
#Create a method addTime which should take two Time objects and add them.
#E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
#Create another method displayTime which should print the time.
#Also create a method displayMinute which should display the total minutes in the Time.
#E.g.- (1 hr 2 min) should display 62 minute.
class time:
    def __init__(self,h,m):
        self.h=h
        self.m=m
    def distime(self):
        if self.m>=60:
            self.h+=1
            self.m=self.m-60
            print(f"Time: {self.h}hr and {self.m} min")
        else:
            print(f"time={self.h}hrs:{self.m}min")

    def addTime(self,hr,min):
        min1=min+self.m
        if min1 >= 60:
            hr+=1
            hr1=hr+self.h
            min1=min1-60
            print(f"time: {hr1} hr and {min1}min")
        else:
            hr1=hr+self.h
            print(f"Time:{hr1}hr:{min1}minutes")
    def mindis(self):
        hr2=self.h*60
        t=hr2+self.m
        print(f"total min: {t} minutes")
x=time(5,30)
x.mindis()
x.distime()
x.addTime(1,1)

#5. Write a Person class with an instance variable “age” and a constructor that takes an integer as a
#parameter. The constructor must assign the integer value to the age variable after confirming the
#argument passed is not negative; if a negative argument is passed then the constructor should set
#age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
#methods:
class Person:
    def __init__(self,age,name):
        self.name=name
        if age>0:
            self.age=age
        else:
            self.age=0
            print(f"Age is not valid,setting age to zero.")
    def yearPasses(self,n):
        self.age=self.age+n
        print(f"you are {self.age} old now.")
    def amIold(self):
        if self.age>=13 and self.age<=19:
            print(f"You are a teenager")
        elif self.age<13:
            print("You are young.")
        else:
            print("You are old.")

x=Person(-4,"NAIMA")
x.yearPasses(14)
x.amIold()

