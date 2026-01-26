# Write a program which accept one number from user and return its factorial.

def Factorial(x):
    fact = 1

    for i in range(2,x+1):
        fact = fact * i
    
    return fact

def main():
    a = int(input("Enter the number:"))

    f = Factorial(a)

    print("Factorial :",f)

if __name__ == "__main__":
    main()