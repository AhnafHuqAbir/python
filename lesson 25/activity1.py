class Student:

    grade = 8

    def display(self):
        print("welcome the student of grade", self.grade)

student1 = Student()
print("Grade: ", student1.grade)
student1.display()