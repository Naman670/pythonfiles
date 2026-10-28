# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

size = int(input("Enter the size of the triangle: "))
def print_triangle(size): 
    for i in range(size):
        if i % 2 == 0:
            print("\\*// " * (i+1),end="\n")
        else:
            print("//*\\ " * (i+1))

print_triangle(size)
                      