from functools import reduce

product = lambda x,y : x*y

def main():
    l = int(input("Enter number of elements:"))

    numbers = []

    print("Enter the numbers:")
    for i in range(l):
        val = int(input())
        numbers.append(val)
    
    print("Numbers :",numbers)

    pro = reduce(product,numbers)

    print("Product of numbers:",pro)

if __name__ == "__main__":
    main()