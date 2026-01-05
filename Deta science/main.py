import numpy as np

data_type = [('name', 's15'), ('class', 'int'), ("Height", "float")]
students_deatails = [('Rafsan', '8', 5.9), ('Partho', '8', 5.7), ("Muntakim", "8", 4.9)]

students = np.array(students_deatails, dtype = data_type)
print("Original Array : ")
print(students)
print("\n")
print("Sort by Height : ")
sorted_by_height = np.sort(students, order='Height')