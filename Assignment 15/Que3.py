checkOdd = lambda x : x % 2 == 1

def main():
    l = int(input("Enter the number of elements:"))

    numbers = []

    print("Enter the numbers:")
    for i in range(l):
        val = int(input())
        numbers.append(val)
    
    print("Numbers :",numbers)
    
    evenList = list(filter(checkOdd,numbers))

    print("Odd numbers :",evenList)

if __name__ == "__main__":
    main()