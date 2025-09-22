class Preson(object):
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
    def desplay(self):
        print(self.name)
        print(self.id_number)

class employee( Preson ):
    def __init__(self, name, id_number, salary, post):
        self.salary = salary
        self.post = post
        Preson.__init__(self, name, id_number)

a = employee("Salman Khan", 908765, 90000, "Actor")
a.desplay()