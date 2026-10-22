from pom.base import base # importing base class

nam="multiuse class variable" # Global variable
print("hello",nam)
nameforbase="base class variable" # global variable

class multiuse(base): # class definition
    def __init__(self): # initializer method
        self.name = nam
        self.nameforbase = nameforbase 
        super().__init__(nameforbase) # calling base class initializer  
        

    def by(self): # method to print
        print("multiuse class")

