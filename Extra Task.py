#create a list of given structure and get access list as provided.
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x[5][:4])
print(x[6:8])
print(x[0::2])
print(x[::-1])
print(x[5][5][0:1])
print(x[0:0])
#create a list of thounsand numbers using range and xrange, and see the difference between each other
 #using range
x1=list(range(1000))
print(x1)
 #using xrange
#python xrange also does the same functionality as range. This is available in python 2.x.If we need to generate a list of small range then xrange is the best option otherwise, xrange take more time and memory compared to range.
#xrange is more like generator which gives values on demand.

#How tuple is benificial compared to list?

 #Once we create tuple the values that we have provided are not changable. So, compared to list the chance for mishandling or changes in values due to
 #unexpected operations can be avoided by using tuples.


#Write apyrthon program to iterate through the list of numbers in range of 1,100 and print the number whuch is divisible by
#  3 and multiple of 2

for i in range(1,101):
    if i%3==0 and i%2==0:
        print (i)
#Write a program to reverse a string and print only the vowel alphabet if it exists in the string with their index
inputs=input("Enter your input: ")
vowels=["a","e","i","o","u"]
rev=inputs[::-1]
print(rev)
print("Index Value")
for i,j in enumerate(rev) :
    if j in vowels:
        print(f"{i}     {j}")

# Write a program in python  to iterate through a string 'hello my name is abcde' and print the string which is having even length.

s="hello my name is abcde"
l=s.split()
d=[]
for i in l:
    d.append(len(l))
for j in l:
    if len(j)==max(d):
        print(j)

#Write a program in python to print the pair of numbers whose sum is equal to the result number that lets say 8.
x=[1,2,3,4,5,6,7,8,9,-1]
l=len(x)
p=[]
q=[]
for i in range(l-1):
    for j in range(l):
        if i+j==8:
            if i not in p and j not in p:
                p.append(i)
                p.append(j)
                q.append([i,j])
print(q)
#Write a program in python to completr following task
even_list=[]
odd_list=[]
for i in range(5):
    x=int(input(f"Enter {i} th number in between 1 and 50 : "))
    if x%2==0:
        even_list.append(x)
    else:
        odd_list.append(x)
sum1=sum(even_list)
sum2=sum(odd_list)

if sum1>sum2:
    print(f"List of even number has highest sum, Even list:{even_list}")
else:
    print(f"List of odd number has highest sum, odd list:{odd_list}")
#Write a program to find out the occurance of specific charecter from an alphanumeric string.
sample_input="12abcbacbaba344ab"
import numpy as np
sample_input="12abcbacbaba344ab"
li=[]
for i in sample_input:
    if  not i.isdigit():
        li.append(i)
u=np.unique(li)
for i in u:
    print(f"{i} has occured {li.count(i)} times.")

#Generate and print another tuple whose values are numbers in the given tuple

tup1=(1,2,3,4,5,6,7,8,9,10)
s1,s2,s3,s4,s5,s6,s7,s8,s9,s10=1,2,3,4,5,6,7,8,9,10
list1=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
list2=[]
for i in range(len(list1)):
    if i%2==0:
        list2.append(i)
tup2=tuple(list2)
print(f"Second tuple: {tup2}")



