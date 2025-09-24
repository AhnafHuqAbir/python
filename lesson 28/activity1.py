class myClass:

    __privateVar = 27 ;
    def __privMeth(self):
        print("I am inside class myClass")
    
    def hello(self):
        print("private Variable value:",myClass. __privateVar)
    
foo = myClass()
foo.hello()
foo. __privMeth()