from functools import reduce

def checkPrime(x):
    for i in range(2,x//2+1):
        if(x % i == 0):
            return False
    
    return True

def mul2(x):
    return (x * 2)

def max(m,x):
    if(x > m):
        return x
    
    else:
        return m

def main():
    l = int(input("Enter the number of elements : "))

    numbers = []

    print("Enter the elements :")
    for i in range(l):
        val = int(input())
        numbers.append(val)
    
    print("Input List :",numbers)

    fnumbers = list(filter(checkPrime,numbers))
    print("List after filter :",fnumbers)

    mnumbers = list(map(mul2,fnumbers))
    print("List after map :",mnumbers)

    rnumbers = reduce(max,mnumbers,mnumbers[0])
    print("Output of reduce :",rnumbers)

if __name__ == "__main__":
    main()