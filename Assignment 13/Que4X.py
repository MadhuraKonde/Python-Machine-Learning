def convertBinary(x):
    bin = ""

    if(x == 0):
        bin = 0
    
    while(x != 0):
        dig = x % 2
        bin = str(dig) + bin
        x = x // 2
    
    return bin

def main():
    a = int(input("Enter a number:"))

    binary = convertBinary(a)

    print("Binary Equivalent:",binary)

if __name__ == "__main__":
    main()