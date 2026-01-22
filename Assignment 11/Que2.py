def DigitCount(x):
    dig = 0

    while(x!=0):
        dig = dig + 1

        x = x//10
    
    return dig

def main():
    a = int(input("Enter a number:"))
    
    if(a == 0):
        d = 1
    
    else:
        if(a<0):
            a = -a
        
        d = DigitCount(a)

    print(d)

if __name__ == "__main__":
    main()