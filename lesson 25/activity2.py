class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    
car1 = Vehicle(200, 25)
car2 = Vehicle(170, 28)

print("car1 max speed : ", car1.max_speed)
print("Car 1 mileage : ", car1.mileage)

print()

print("car2 max speed : ", car2.max_speed)
print("Car 2 mileage : ", car2.mileage)