multiplication = lambda x,y : x*y

def main():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))

    mul = multiplication(a,b)

    print("Multiplication :",mul)

if __name__ == "__main__":
    main()