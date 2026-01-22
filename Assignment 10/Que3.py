def factorial(x):
    fact = 1

    for i in range(2,x+1,1):
        fact = fact * i
    
    return fact

def main():
    a = int(input("Enter a number:"))

    f = factorial(a)

    print(f)

if __name__ == "__main__":
    main()