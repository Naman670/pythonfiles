def main(x):
   # x=input("Enter a number: ")
    if is_even(int(x)) and is_even_new(int(x)) and is_even_new_rt(int(x)):
        print("The number is even.")
    else:
        print("The number is odd.")

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
def is_even_new(num):
    return True if num % 2 == 0 else False

def is_even_new_rt(num):
    return num % 2 == 0 
main(5)