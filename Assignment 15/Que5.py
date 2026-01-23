from functools import reduce

maximum = lambda x,y : x if (x>y) else y

def main():
    l = int(input("Enter number of elements:"))

    numbers = []

    print("Enter the numbers:")
    for i in range(l):
        val = int(input())
        numbers.append(val)
    
    print("Numbers :",numbers)

    max = reduce(maximum,numbers)

    print("Addition of numbers:",max)

if __name__ == "__main__":
    main()