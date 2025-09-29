class BMW:
    def country(self):
        print("Bmw is a German car")

    def price(self):
        print("Bmw's lowest price is 1 crore")

    def top_speed(self):
        print("BMW's top speed is 300km/hr")

    def best_car(self):
        print("Bmw's one of the best car is BMW x7 but people love BMW m5 more")

    def about(self):
        print("BMW is a car brand but BMW also create motorbikes. Bmw's best motorbike is BMW S1000RR but people love BMW1000 RRR more. I like BMWM5 car because my family has a BMWM5 car.")

class Farrari:
    def country(self):
        print("Farrari is an Italian car brand")

    def price(self):
        print("Farrari's lowest price is 2 crore")
    
    def top_speed(self):
        print("Farrari's top speed is 340km/hr")

    def best_car(self):
        print("Farrari's one of the best car is Farrari LaFerrari")

    def about(self):
        print("Farrari is a car brand but Farrari also create motorbikes. Farrari's best motorbike is Farrari S1000RR.")

def car_information(car):
    car.about()
    car.country()
    car.price()
    car.top_speed()
    car.best_car()
    car.about()
    print(":]" * 50)

Bmw_car = BMW()
Farrari_car = Farrari()

for car in (Bmw_car, Farrari_car):
    car_information(car)