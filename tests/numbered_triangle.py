
size = int(input("Enter the size of the triangle: "))
def print_triangle(size): 
    for i in range(1,size+1):
            for j in range(1,i+1):
                print(i * j,end=" ")  
            print()
       
print_triangle(size)
                      