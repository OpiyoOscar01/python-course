#Writing and reading to files.
# with open("student_records.txt", "w") as file:
#     file.write("I am student 3\n")
#     file.write("I am student 4.\n")  
with open("student_records.txt", "a") as file:
    file.write("I am student 5\n")
    file.write("I am student 6.\n") 