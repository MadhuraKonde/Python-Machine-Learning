from functools import reduce

checkeven = lambda x : (x % 2 == 0)

square = lambda x : (x * x)

add = lambda x,y : (x + y)

def main():
    l = int(input("Enter the number of elements : "))

    numbers = []

    print("Enter the elements :")
    for i in range(l):
        val = int(input())
        numbers.append(val)
    
    print("Input List :",numbers)

    fnumbers = list(filter(checkeven,numbers))
    print("List after filter :",fnumbers)

    mnumbers = list(map(square,fnumbers))
    print("List after map :",mnumbers)

    rnumbers = reduce(add,mnumbers)
    print("Output of reduce :",rnumbers)

if __name__ == "__main__":
    main()