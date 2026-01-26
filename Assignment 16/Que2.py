def ChkNum(n):
    if(n % 2 == 0):
        print("Even Number")
    
    else:
        print("Odd Number")

def main():
    a = int(input("Enter a number:"))
    ChkNum(a)

if __name__ == "__main__":
    main()