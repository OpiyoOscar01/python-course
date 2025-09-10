name="James"
age=24
#Approach 1:
message=f"My name is {name} and I am {age} years old."
print(message)
formatted_message=f"My name is {name} and I am {age} years old."
print(formatted_message)

#Approach 2: Using the format() method
email="example@gmail.com"
message2="My name is {} and I am {} years old. My email is {}.".format(name,age,email)
print(message2)