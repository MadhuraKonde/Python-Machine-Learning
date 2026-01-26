def minlist(l):
    min = l[0]

    for i in l:
        if(i < min):
            min = i
    
    return min

def main():
    n = int(input("Number of elements : "))

    numbers = []

    print("Input Elements :")
    for i in range(n):
        val = int(input())
        numbers.append(val)
    
    min = minlist(numbers)

    print("Minimum number :",min)

if __name__ == "__main__":
    main()