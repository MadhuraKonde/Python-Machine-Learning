addition = lambda x,y : x+y

def main():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))

    add = addition(a,b)

    print("Addition :",add)

if __name__ == "__main__":
    main()