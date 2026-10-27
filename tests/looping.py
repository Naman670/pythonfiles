# while
# i +=1
# i -=1
# for
# list [1,2,3,4,5] with for loop
# range(1,10) with for loop

#print("while loop" * 3)
#print("while loop\n" * 3)
#print("while loop\n" * 3,end="")
#print("while loop\n" * 3,end="###-####",sep="#nam#")

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

def main() :
    number = get_number ( )
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()

students = ["Hermione", "Harry", "Ron"]

for i in range (len(students)):
    print(i + 1, students [i])

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}



print(students ["Hermione"] )
print(students ["Harry"])
print(students ["Ron"])
print(students ["Draco"])




for student in students:
    print(student)# this will print the keys of the dictionary
    print(students[student])# this will print the values of the dictionary
    print(student,students[student], sep="::::> ")# this will print the keys and values of the dictionary with a separator "::::> "



# list of dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]



for student in students:
    print(student ["name"], student ["house"], student ["patronus"], sep=", ")