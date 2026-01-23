def convertBinary(x):
    p = 0
    n = 2**p

    while(x >= n):
        p = p + 1
        n = 2**p

    temp = x
    bin = 0

    for i in range(p-1,-1,-1):
        n = 2**i
        bin = bin * 10

        if(temp >= n):
            bin = bin + 1
            temp = temp - n
    
    return bin

def main():
    a = int(input("Enter a number:"))

    binary = convertBinary(a)

    print("Binary Equivalent:",binary)

if __name__ == "__main__":
    main()