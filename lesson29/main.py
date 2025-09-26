class square:
    def __init__(self, side):
        self.side = side
    
    def area(self):
        print(f'my area is : {self.side ** 2}')

class circle:
    def __init__(self, raddius):
        self.raddius = raddius

    def area(self):
        print(f'my area is : {3.14 * self.raddius ** 2}')

s = square(7)
c = circle(7)

for shape in (s, c):
    shape.area()