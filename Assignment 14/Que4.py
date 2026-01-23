#minimum = lambda x,y : min(x,y)
minimum = lambda x,y : x if (x<y) else y

def main():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))

    min = minimum(a,b)

    print("Smaller number is :",min)

if __name__ == "__main__":
    main()