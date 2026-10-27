def main():
    size = int(input("Enter the size of the square: "))
    print_square(size)
    print ("------------#--------", end="\n",sep="")
    print_square2(size)
    print ("------------#--------", end="\n",sep="")
    print_square3(size)
    print ("------------#--------", end="\n",sep="")
    print_square4(size)

def print_square(size):
        for i in range(size):
            for j in range(size):
                print ("#", end="")
            print()



def print_square2(size):
    for i in range(size):
        print("#" * size,end="\n")

def print_square3(size):
    for i in range(size):
        print("#" * size,end="\n")
        size -=1

def print_square4(size):
    for i in range(size):
        print(" " * (size-1), "#" * (i+1), sep="", end="\n")
        
        
        size -=1

main()