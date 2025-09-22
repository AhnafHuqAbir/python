class Vehicle:
    def __init__(self, name, max_speed, mileage):
         self.name = name
         self.max_speed = max_speed
         self.mileage = mileage

class bus(Vehicle):
    pass

school_bus = bus("school_Nabil", 180, 12)
print("Vehicle Name:", school_bus.name, "Speed:", school_bus.max_speed, "Mileage:", school_bus.mileage)    