from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self, x):
        print("Passed value: ", x)

    def task(self):
        print("I am an abstract method")

class test_class(Absclass):
    def task(self):
        print("I am the implementation of abstract method")

test_obj = test_class()
test_obj.task()
test_obj.print(100)