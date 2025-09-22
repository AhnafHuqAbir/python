class Bird:
    def __init__(self):
        print("Bird is ready")
    
    def WhoIsThis(self):
        print("Bird")

    def swim(self):
        print("Swim fast")

class Penguin(Bird):
    def __init__(self):
        super(). __init__()
        print("Penguin is ready")
    def WhoIsThis(self):
        print("Penguin")
    def run(self):
        print("Run fast")

peggy = Penguin()
peggy.WhoIsThis()
peggy.swim()
peggy.run()