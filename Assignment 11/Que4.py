def DigitReverse(x):
    rev = 0

    while(x!=0):
        dig = x % 10
        rev = rev*10 + dig
        x = x // 10
    
    return rev

def main():
    a = int(input("Enter a number:"))

    if(a < 0):
        a = -a
    
    arev = DigitReverse(a)

    print(arev)

if __name__ == "__main__":
    main()