
class Vehicle:
    def __init__(self, name, capacity, fare_per_person):
        self.name = name
        self.capacity = capacity
        self.fare_per_person = fare_per_person

    def fare(self):
        return self.capacity * self.fare_per_person


class Bus(Vehicle):
    def fare(self):
        # Get base fare from parent
        total_fare = super().fare()
        # Add 10% extra charge
        total_fare += total_fare * 0.10
        return total_fare

vehicle1 = Vehicle("Car", 4, 50)
bus1 = Bus("School Bus", 50, 20)

print(f"Vehicle Fare ({vehicle1.name}): {vehicle1.fare()} Tk")
print(f"Bus Fare ({bus1.name}): {bus1.fare()} Tk")
