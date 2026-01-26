def maxlist(l):
    max = l[0]

    for i in l:
        if(i > max):
            max = i
    
    return max

def main():
    n = int(input("Number of elements : "))

    numbers = []

    print("Input Elements :")
    for i in range(n):
        val = int(input())
        numbers.append(val)
    
    max = maxlist(numbers)

    print("Maximum number :",max)

if __name__ == "__main__":
    main()