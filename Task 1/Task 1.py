#assigning 3 different data type to 3 variable in a single line
a,b,c="naima",4.6,8
#assigning complex number and a number
c,d=(1+4j),6
# swaping using third variable
e=6
f=7
temp=f
f=e
e=temp
print(e,f)

#printing in python.3.x
g=input("Enter your name: ")
print(g)
#Adding 2 numbers and then printing result after adding 30
h= int(input("Enter a numbrts in between 1 and 10: "))
i= int(input("Enter a numbrts in between 1 and 10: "))
j = (h+i)
result= (j+30)
print(result)
#checking type of entered value

inp= input("enter a string or integer or float: ")

if isinstance(inp,int):
    print("The data type of input value is integer ")
elif isinstance(inp,str):
    print("The data type of inut value is string ")
elif isinstance(inp, float):
    print("The data type of input value is float")
# Different cases
word="naima valiyaparambil rajendran"
k="naimaValiyaparambilRajendran"# lower camel
l= "NaimaValiyaparambilRajendran"#upper camel case
m="naima_valiyaparambil_rajendran"#snake case

# re-assign variable with different value
o="naima"
print(o)
print(id(o))
o=9
print(id(o))
print(o)


