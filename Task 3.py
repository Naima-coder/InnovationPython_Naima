#(1)create a list of different data type
l=["name",(1+8j),5.4,8,"consultadd"]
#(2)Create a list of size 5 and excecute slicing structure
list=[1,2,4,7,8,9]
print(list[1:3:1])
#(3)write a program to get the sum and multiply of all the items in a given list
p=[1,2,3,4,5]
a=0
b=1
for i in p:
    a=a+i
    b=b*i
print(f"sum:{a}")
print(f"Multiplication:{b}")
#(4) Find the largest and smallest number from a given list
p=[0,7,4,3,89]
print(f"minimum value: {min(p)}")
print(f"maximum value: {max(p)}")

#(5)Create a new list of elements such that it contains the specified numbers after removing the even numbers from a predefined list.
l3=[1,2,3,4,6,34,8,9,6]
print(f"original list:{l3}")
a=5
for i,j in enumerate(l3):
    if j%2==0:
        l3[i]=a
print (f"List after modification :{l3}")
#create a list of elements such that it  contains the squares of the first and last 5 elements between 1 and 30 (both included)
list=[]
for i in range(1,31):
    if i <=5:
        p=i*i
        list.append(p)
    elif 6<=i<25:
        pass
    else:
        q=i*i
        list.append(q)
print(list)
#write a program to replace the last element in a list with another list
sample=[1,3,5,7,9,10]
ext=[2,4,6,8]
print(f"list-1:{sample} ")
print(f"list-2:{ext} ")
samp=sample[0:5]
last=samp+ext
print(f"last list:{last} ")
#write a program to concatenate 2 dictionary.
s1={1:10,2:20}
s2={3:30}
s1.update(s2)
print(f"Concatenated dictionary:{s1}")
#9)create a dictionary that contains numbers in the form (x:x*x), where x takes values b/w 1 and n (both 1 and n included)
d=[1,2,3,4,5,6]
list3=[]
for i in d:
    p=i*i
    list3.append(p)
dict1=dict(zip(d,list3))
print(dict1)
#10)write a program which acceps a sequence of comma-separated numbers from console and generates a list and a tuple which contains every number in the form of string.
x = input("Enter numbers: ")
x1 = x.split(",")
x2 = tuple(x1)
print(x1, x2)



