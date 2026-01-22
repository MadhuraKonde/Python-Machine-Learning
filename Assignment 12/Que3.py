def Addition(x,y):
    return x+y

def Subtraction(x,y):
    return x-y

def Multiplication(x,y):
    return x*y

def Division(x,y):
    return x/y

def main():
    print("Enter two numbers:")
    a = int(input())
    b = int(input())

    print("Addition :",Addition(a,b))
    print("Subtraction :",Subtraction(a,b))
    print("Multiplication :",Multiplication(a,b))
    print("Division :",Division(a,b))

if __name__ == "__main__":
    main()