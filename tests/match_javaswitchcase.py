x= input("Enter a number between 1 and 5: ")
match x:
    case "1"|"2"|"3"|"4"|"5":
        print("You entered a number between 1 and 5.")
    case _:
        print("You entered something else.")    