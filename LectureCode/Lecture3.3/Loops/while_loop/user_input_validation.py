
while True:
  user_age=input("Enter your age(or type 'exit' to quit): ")
  if user_age.lower()=='exit':
    print("Exiting the program.....")
    print("Good bye.See you again")
    break
  try:
    user_age=int(user_age)
    if user_age<0:
      print("Age cannot be negative. Please enter a valid age.")
    else:
      print(f"Your age is: {user_age}")
    break
  except ValueError:
    print("Invalid input. Please enter a valid age.")