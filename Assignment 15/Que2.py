checkEven = lambda x : x % 2 == 0

def main():
    l = int(input("Enter the number of elements:"))

    numbers = []

    print("Enter the numbers:")
    for i in range(l):
        val = int(input())
        numbers.append(val)
    
    print("Numbers :",numbers)
    
    evenList = list(filter(checkEven,numbers))

    print("Even numbers :",evenList)

if __name__ == "__main__":
    main()