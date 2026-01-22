def cube(x):
    c = x**3
    return c

def main():
    a = int(input("Enter a number:"))

    c = cube(a)

    print("Cube of",a,"=",c)

if __name__ == "__main__":
    main()