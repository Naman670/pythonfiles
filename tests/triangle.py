def main():
    size = int(input("Enter the size of the triangle: "))
    print()
    print_triangle(size)
    print()
    print_triangle_reverse(size)


def print_triangle(size):
    for i in range(size):
        print(" " * (size-1), "* " * (i+1), sep="", end="\n")
        size -=1


def print_triangle_reverse(size):
    for i in range(size):
        print(" " * (i), "* " * (size), sep="", end="\n")
        size -=1


main()