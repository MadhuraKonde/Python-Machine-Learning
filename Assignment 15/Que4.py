from functools import reduce

addition = lambda x,y : x+y

def main():
    l = int(input("Enter number of elements:"))

    numbers = []

    print("Enter the numbers:")
    for i in range(l):
        val = int(input())
        numbers.append(val)
    
    print("Numbers :",numbers)

    add = reduce(addition,numbers)

    print("Addition of numbers:",add)

if __name__ == "__main__":
    main()