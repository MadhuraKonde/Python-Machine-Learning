def addlist(l):
    sum = 0

    for i in l:
        sum = sum + i
    
    return sum

def main():
    n = int(input("Number of elements : "))

    numbers = []

    print("Input Elements :")
    for i in range(n):
        val = int(input())
        numbers.append(val)
    
    addition = addlist(numbers)

    print("Addition :",addition)

if __name__ == "__main__":
    main()