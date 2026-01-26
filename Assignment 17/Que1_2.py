'''
Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication 
and Div() for division. All functions accepts two parameters as number and perform the operation. Write on python program which call all 
the functions from Arithmetic module by accepting the parameters from user.
'''

from Arithmetic import Add,Sub,Mult,Div

def main():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))

    add = Add(a,b)
    print("Addition :",add)

    sub = Sub(a,b)
    print("Subtraction :",sub)

    mul = Mult(a,b)
    print("Multiplication :",mul)

    div = Div(a,b)
    print("Division :",div)

if __name__ == "__main__":
    main()