# #Syntax:
# def function_name(arguments):
#   pass #Logic.

# #eg:Function to great a user
# def great_user(name):
#   print(f"Hello,{name}")

# great_user("Joel.")
  
# #Function conventions: The function name should be descriptive and written using snake_case, shouldn't be too short or too long.
# def deposit():
#   pass
# def x():
#   pass

# def calculate_area(length,width):
#   pass

#function width parameters.
# def introduce_user(name,job,city):
#   print(f"Hello, I am {name}, a {job}. I live in {city}")

# introduce_user("Alice","Teacher","New York")

#Function with default parameters.

# def great_user(name,title="Mr/Mrs"):
#   print(f"Hello I am {title} {name}.")

# great_user("Joel")
# great_user("Mark","Dr.")

#Keyword arguments.
import math
from unittest import result
from arrow import get


def book_flight(passenger,destination,return_date):
  print(f"{passenger}: Destination:{destination};Return Date:{return_date}")

# #By default,we follow positional Argument when passing argument values.
# book_flight("Joel","Tokyo","Tue 23rd Jan 2027")
# #When using keyword arguments,positioning does not matter.
# book_flight(return_date="Wed 23rd Jan 2029.",passenger="Joel",destination="Beijing")

#Variable length Arguments.
#Eg. A function the computes the sum of numbers passed to it.

# def compute_sum(*numbers):
#   sum=0
#   for number in numbers:
#     sum+=number
#   return sum
# #Call the function;
# result=compute_sum(1,3,4,6,9,10,-38)
# print(f"The sum after computation is {result}.")

#Return values:
# def add_numbers(a,b,c):
#   return a+b+c

# summation=add_numbers(2.4,5,8)
# print(summation)

# def get_full_name(first_name,last_name):
#   return first_name+" "+last_name

# full_name=get_full_name("Erick","Serujoji")
# print(full_name)

# #Returning multiple values.
# def get_name_parts(full_name):
#   name_parts=full_name.split()
#   first_name=name_parts[0]
#   last_name=name_parts[-1]
#   return last_name,first_name

# print(get_name_parts("Mark Jones"))

#Variable scope
#1.Local/function scope==This variable is only accessible within the function(Block of code) within which it's defined.
#Global scope==This variable can be accessed from any part of your program/code.
credit_points=12# The variable has a global scope.

# def compute_grade(score):
#   new_score=score+5 #Variable has a local/function scope
#   return new_score
# print(compute_grade(67))

# print(credit_points)

# #Correction:

# def calculate_marks(*marks):
#   sum=0
#   for score in marks:
#     sum+=score
#   return sum
# total_score=calculate_marks(23,73,87,90)
# print(f"The total score is {total_score}.")

#Return Values.

# def add_number(a,b):
#   result=a+b
#   return result

# sum =add_number(3,6)
# print(f"The result of the summation is {sum}")

# def process_data(name,age):
#   info=f"Name:{name},Age:{age}"
#   return info
# processed_info=process_data("Joel",29)
# print(processed_info)

#Returning multiple values.
# def get_name_parts(full_name):
#   name_parts=full_name.split()
#   print(name_parts  )
#   first_name=name_parts[0]
#   last_name=name_parts[-1]
#   return last_name,first_name

# get_name_parts("Alice Nabubi")

#Early return.

# def divide_numbers(a,b):
#   if b==0:
#     print("Error:Division by zero is not allowed.")
#     return None
#   return a/b

# result1=divide_numbers(10,5)
# print(f"Result1:{result1}")

# result2=divide_numbers(8,0)
# print(f"Result2:{result2}")

#Variable scope.
#Local/function scope.

# def calculate_area(length,width):
#   x=7 #Variable has a local/function scope.
#   area=length*width #Variable has a local/function scope.
#   return area
# room_area=calculate_area(10,7)
# print(f"The area of the room is {room_area}.")

#Global variable scope.
# PI=3.14159 #Variable has a global scope.

# def area_of_circle(radius):
#   area=PI*math.pow(radius,2)
#   # area=PI*radius**2
#   return area

# area1=area_of_circle(36)
# print(f"The area of the circle is {area1} meters squared.")
# print(f"The value of the constant PI={PI}")

#Anonymous/lambda/Nameless Functions.
# cube=lambda x:x**3
# print(f"The cubic result is: {cube(2)}")

processed_data=lambda first_name,age:f"Hello {first_name}.You're are {age} years old."

print(processed_data("Joel",98))