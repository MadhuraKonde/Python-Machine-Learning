from functools import reduce

checkEven = lambda x : x % 2 == 0

count = lambda x,y : x+1

def main():
    l = int(input("Enter the number of elements:"))

    numbers = []

    print("Enter the numbers:")
    for i in range(l):
        val = int(input())
        numbers.append(val)
    
    print("Numbers :",numbers)
    
    evenList = list(filter(checkEven,numbers))

    evenCount = 0
    evenCount = reduce(count,evenList,evenCount)

    print("Count of even numbers :",evenCount)

if __name__ == "__main__":
    main()