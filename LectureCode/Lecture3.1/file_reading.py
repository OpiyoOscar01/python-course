# with open("student_records.txt", "r") as file:
#     file_content = file.read()
#     print(file_content)

#Approach 1:Reading Line by line.
# with open("student_records.txt", "r") as file:
#     # lines = file.readlines()
#     for line in file:
#         print(line.strip())  # strip() is used to remove leading/trailing whitespace characters

#Approach 2: Using readlines()
with open("student_records.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() is used to remove leading/trailing whitespace characters