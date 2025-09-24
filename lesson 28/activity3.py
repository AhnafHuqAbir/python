class Computer:
    def __init__(self):
        self.__maxprice = 1000

    def sell(self):
        print(f"selling price: {self. __maxprice}")

    def setMaxPrice(self, price):
        self. __maxprice = price

J = Computer()
J.sell()

J. __maxprice = 1200
J.sell()

J.setMaxPrice(1200)
J.sell()