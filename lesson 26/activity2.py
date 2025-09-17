class Employee:

    def __init__(self):
        print("Employee created")

    def __del__(self):
        print("Destructor called, Employee deleted.")

def create_obj():
    print("Making obj...")
    obj = Employee()
    print("Function Endind......")
    return obj

print("creating create_obj() function.....")
obj = create_obj()
print("Program Endding......")