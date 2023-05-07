#this is a simple clculator Program to understand class and methods

class calculator:
    # this is the class and the methods are declared inside it

    def substraction(self, a, b):
        #this is a method described for substraction using user defined variables
        if a > b:
            return a-b
        else:
            return b-a

    def addition(self, a, b):
        # this is a method described for addition using user defined variables
        return a+b

    def multiplication(self, a, b):
        # this is a method described for multiplication using user defined variables
        return a*b

    def devision(self, a, b):
        # this is a method described for devision using user defined variables
        if a > b:
            return a/b
        else:
            return b/a

my_calc = calculator()

def oparation(ch):
    #this is a simple function to call the methods described in the class calculator
    if ch == "add":
        res = my_calc.addition(a, b)
        print("the result is", res)
    elif ch == "substract":
        res = my_calc.substraction(a, b)
        print("the result is", res)
    elif ch == "multiply":
        res = my_calc.multiplication(a, b)
        print("the result is", res)
    elif ch == "devide":
        res = my_calc.devision(a, b)
        print("the result is", res)


ch = str(input("enter the operation you want to perform (add/substract/multiply/devide)"))

a = int(input("enter 1ST number"))
b = int(input("enter 2nd number"))
oparation(ch)
