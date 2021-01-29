#1. Write a program in Python to find out the character in a string which is uppercase using list
#comprehension.
g="Hello nAIMA"
L=[x for x in g if x==x.upper() and x!=' ']
print(L)
#Write a program to construct a dictionary from the two lists containing the names of students and
#their corresponding subjects. The dictionary should map the students with their respective subjects.
#Let’s see how to do this using for loops and dictionary comprehension.
students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']
dict1=dict(zip(students,subjects))
print(dict1)
  ##Using for loop
students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']
d={}
for i in students:
    for j in subjects:
        p={i:j}
        d.update(p)
print(d)
#Write a program in Python using generators to reverse the string.
#Input String = “Consultadd Training”

def rev(inputs):
    l=len(inputs)
    for i in range(l-1,-1,-1):
        yield inputs[i]


inputs="Consultadd Training"
print(f"input: {inputs}")
for i in rev("consultadd Training"):
    print(i,end="")
#Write a example for decorator
def fun(a,b):
    print(a-b)
def ex(func):
    def inner(a,b):
        if b>a:
            a,b=b,a
        return func(a,b)
    return inner

example=ex(fun)
exa=example(4,1)
