#Program to grade a student based on their marks.
score=36
if score>=90:#Not true
  grade='A'
elif score>=80:
  grade='B'
elif score>=70:
  grade='C'
elif score>60:
  grade='D'
else:
  grade='F'
print(f"Your grade is {grade}")