def Palindrome(x):
    rev = DigitReverse(x)

    if(x == rev):
        return True
    
    return False

def DigitReverse(x):
    rev = 0

    while(x!=0):
        dig = x % 10
        rev = rev*10 + dig
        x = x // 10
    
    return rev

def main():
    a = int(input("Enter a number:"))

    if(Palindrome(a)):
        print("Palindrome")
    
    else:
        print("Not Palindrome")

if __name__ == "__main__":
    main()