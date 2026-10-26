class SquareRoot:
    def __init__(self, number_number):
        self.number = number_number

    def square_root(self, number=None):
        if number is None:
            number = self.number
            return number * number
        else:
            return number * number

    def sq(self, newnumber):
        return newnumber * newnumber


ob = SquareRoot(5)
print("from in it method",ob.number)
result = ob.square_root()
print("from init method",result)
result = ob.square_root(7)
print("from method method",result)

if result % 2 == 0:
    print("even")
else:
    print("odd")

result2 = ob.square_root(6)
print("from square_root method",result2)
if result2  % 2 == 0:
    print("even")
else:
    print("odd")

result3 = ob.sq(3)
print("from sq method",result3)
if result3 % 2 == 0:
    print("even")
else:
    print("odd")
