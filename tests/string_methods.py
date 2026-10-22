name=" john doe "
name=name.strip() # removes leading and trailing whitespace
print(f"name is {name}") # Output: "John Doe"
name= name.capitalize() # capitalizes the first letter of the string
print(f"name is {name}") # Output: "John Doe"
name=name.title() # capitalizes the first letter of each word in the string
print(f"name is {name}") # Output: "John Doe"
name=name.strip().title() # removes leading and trailing whitespace and capitalizes each word
print(f"name is {name}") # Output: "John Doe"



####### int########
x="5"
y="10"
z=x+y # concatenates the two strings
print(f"z is {z}") # Output: "510"  

x= int(5)
y= int(10)
z=x+y # converts the strings to integers and adds them
print(f"int is {z}") # Output: "15"  

print("int is",x+y) # Output: "15"  

### Float###
x= float(77075.894)
y= float(10.934)
z=x+y # converts the strings to integers and adds them
print(f"float is {z:,}") # Output: "7,786.828" 

print("rounding float",round(x+y)) # rounding the float value to nearest integer