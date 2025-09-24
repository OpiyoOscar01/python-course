#Variable-length arguments
#Using *args to accept a variable number of arguments.
def calculate_total_marks(*marks):
  total=0
  for score in marks:
    total+=score
  return total
total_marks=calculate_total_marks(85,90,78,92)
print(f"The total marks obtained are: {total_marks}")
total_marks2=calculate_total_marks(88,76,95,89,91,84)
print(f"The total marks obtained are: {total_marks2}")

def create_student_record(name,**details):
  print(f"Student Name: {name}")
  for key,value in details.items():
    print(f"{key}: {value}")
create_student_record("Alice",age=20,city="New York",major="Computer Science")
create_student_record("Bob",age=22,city="Los Angeles",major="Mathematics",GPA=3.8)
create_student_record("Charlie",age=21,city="Chicago")