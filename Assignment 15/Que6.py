from functools import reduce

minimum = lambda x,y : x if (x<y) else y

def main():
    l = int(input("Enter number of elements:"))

    numbers = []

    print("Enter the numbers:")
    for i in range(l):
        val = int(input())
        numbers.append(val)
    
    print("Numbers :",numbers)

    min = reduce(minimum,numbers)

    print("Addition of numbers:",min)

if __name__ == "__main__":
    main()