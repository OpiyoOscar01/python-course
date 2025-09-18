#We have basically three logical Operators in Python and they are and, or, not
# a=True
# b=False
# c=True
# if a and b:
#     print("Both are True")
# else:
#     print("At least one is False")

age=18
has_license=False
if age>=18 and has_license:
  print("You are eligible to drive.")
if age>=18 or has_license:
  print("You are old enough and  can drive.")

#Use of not operator
if not has_license:
  print("You need a license to drive.")
else:
  print("You have a license to drive.")