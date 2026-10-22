from pom.common import multiuse as multi# importing base class

nam="code1" # Global variable
print("hello,",nam)
print("hello,\"escape qts\"")# using escape quotes
print(f"hello, {nam}")# using f-string
NameError="wrong entry"# global variable

class A: # class definition
    def __init__(self): # initializer method
        self.name = nam,
        self.nameErr = NameError

    def by(self): # method to print
        print("bye")
a = A() # class instance / object creation
a.by() # method call
a.name="code2" # modifying the attribute of the object
print(a.name)
a.name # accessing the attribute of the object
print(a) # printing the object reference
print(a.nameErr)

multi=multi() # class instance / object creation
multi.by() # method call
multi.name=nam # modifying the attribute of the object
print(multi.name)