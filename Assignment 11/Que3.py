def DigitSum(x):
    sum = 0

    while(x!=0):
        dig = x % 10
        sum = sum + dig
        x = x // 10
    
    return sum

def main():
    a = int(input("Enter a number:"))

    if(a < 0):
        a = -a
    
    d_sum = DigitSum(a)
    print(a)
    print(d_sum)

if __name__ == "__main__":
    main()