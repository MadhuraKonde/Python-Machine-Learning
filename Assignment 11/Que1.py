def Prime(x):
    for i in range(2,x//2,1):
        if (x % i == 0):
            return False
    
    return True

def main():
    a = int(input("Enter a number:"))

    if(Prime(a)):
        print("Prime Number")
    
    else:
        print("Not a Prime Number")

if __name__ == "__main__":
    main()