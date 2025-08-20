Student = {'name' : 'Ahnaf', 'grade' : 7, 'address' : "Bangladesh"}
print(Student)

print('name-', Student['name'])
Student['subjects'] = ['Math', 'science']
print(Student)
Student['grade'] = 8
print(Student)

for key, value in Student.items():
    print(key, ":", value)