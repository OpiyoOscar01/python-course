#Nested Conditions=A conditional inside another conditional.
age=12
has_license=False
if age>=18:
    if has_license:
      print("You can drive") 
    else:
      print("You need a license to drive")
else:
  print("You are too young to drive")