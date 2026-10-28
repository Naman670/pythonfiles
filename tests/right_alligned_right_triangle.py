size = int(input("Enter the size of the triangle: "))

def print_right_aligned_triangle(size):
    for i in range(size):
        print(" " * (size-1),"*" * (i+1))
        size -= 1



print_right_aligned_triangle(size)