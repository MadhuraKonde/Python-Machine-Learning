from functools import reduce

limit = lambda x : (x >= 70 and x <= 90)

inc10 = lambda x : (x + 10)

pro = lambda x,y : (x * y)

def main():
    l = int(input("Enter the number of elements : "))

    numbers = []

    print("Enter the elements :")
    for i in range(l):
        val = int(input())
        numbers.append(val)
    
    print("Input List :",numbers)

    fnumbers = list(filter(limit,numbers))
    print("List after filter :",fnumbers)

    mnumbers = list(map(inc10,fnumbers))
    print("List after map :",mnumbers)

    rnumbers = reduce(pro,mnumbers)
    print("Output of reduce :",rnumbers)

if __name__ == "__main__":
    main()