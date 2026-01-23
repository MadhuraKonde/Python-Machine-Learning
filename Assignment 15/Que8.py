divisible = lambda x : (x % 3 == 0) and (x % 5 == 0)

def main():
    l = int(input("Enter number of elements:"))

    numbers = []

    print("Enter the numbers:")
    for i in range(l):
        val = int(input())
        numbers.append(val)
    
    print("Numbers :",numbers)

    divList = list(filter(divisible,numbers))

    print("Numbers divisible by 3 & 5 :",divList)

if __name__ == "__main__":
    main()