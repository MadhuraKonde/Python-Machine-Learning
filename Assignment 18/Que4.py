def freqlist(l,n):
    f = 0

    for i in l:
        if(i == n):
            f += 1
    
    return f

def main():
    n = int(input("Number of elements : "))

    numbers = []

    print("Input Elements :")
    for i in range(n):
        val = int(input())
        numbers.append(val)
    
    no = int(input("Enter the number:"))

    freq = freqlist(numbers,no)

    print("Frequency :",freq)

if __name__ == "__main__":
    main()