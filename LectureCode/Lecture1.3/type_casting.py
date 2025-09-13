#Type casting is the process of converting one data type to another data type.
#Types:
#1. Implicit type casting is done by the Python interpreter automatically.
#2. Explicit type casting is done by the programmer manually.
#Implicit type casting
x=20 #Integer
y=2.5 #Float
z=x+y
print(z) #Output: 22.5=Float
print(type(z)) #Output: <class 'float'>

#Explicit type casting
a=10 #Integer
b=3.5 #Float
c=int(b) #Convert float to integer
print(c) #Output: 3
string_number=str(a)
print(string_number) #Output: '10'
print(type(string_number)) #Output: <class 'str'>