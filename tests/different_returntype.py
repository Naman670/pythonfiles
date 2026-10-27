name="some name" # Global variable
flag=False
num=0
class different_returntypes:
    def __init__(self):
        self.name=name
        self.flag=flag
        self.num=num
    def return_string(self):
        return self.name
    def return_boolean(self):
        return self.flag
    def return_integer(self):
        return self.num

df=different_returntypes()    
df.return_boolean()
print(df.return_boolean())
df.return_integer()
print(df.return_integer())
df.return_string()
print(df.return_string())
###############################################3
df.name="naman"
df.flag=True
df.num=42
df.return_boolean()
print(df.return_boolean())
df.return_integer()
print(df.return_integer())
df.return_string()
print(df.return_string())
