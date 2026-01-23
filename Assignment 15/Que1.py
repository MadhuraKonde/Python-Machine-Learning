square = lambda x : x*x

def main():
    l = int(input("Enter the number of elements:"))

    numbers = []

    print("Enter the numbers:")
    for i in range(l):
        val = int(input())
        numbers.append(val)

    print("Numbers :",numbers)

    sqlist = list(map(square,numbers))

    print("Square of numbers :",sqlist)

if __name__ == "__main__":
    main()