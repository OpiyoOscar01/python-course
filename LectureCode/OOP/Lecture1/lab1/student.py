class Student:
    def __init__(self, name, grade):
        self.name = name    # attribute
        self.grade = grade  # attribute

    def study(self):
        print(f"{self.name} is studying.")

    def show_grade(self):
        print(f"{self.name}'s grade is {self.grade}.")

# Create objects
student1 = Student("Alice", "A")
student2 = Student("Bob", "B")

# Access attributes and methods
print(student1.name)   # Alice
student2.study()       # Bob is studying.
student1.show_grade()  # Alice's grade is A.
