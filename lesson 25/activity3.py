class Parrot:

    species = "Bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = Parrot("Blu", 7)
print("{} is a {} and it's age is {}".format(blu.name, blu.species, blu.age))

woo = Parrot("Woo", 4)
print("{} is a {} and it's age is {}".format(woo.name, woo.species, woo.age))