size = int(input("Enter the size of the triangle: "))
def print_triangle(size): 
    for i in range(size):
      print("* " * (i+1))
    for j in range(size):
      
      print(" " * size," " * (size-1),"* " * (j+1))
    size -= 1
       

print_triangle(size)