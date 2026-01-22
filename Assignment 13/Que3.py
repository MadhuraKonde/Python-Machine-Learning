def perfect(x):
    sum = 0
    for i in range(1,(x//2)+1,1):
        if(x % i == 0):
            sum = sum + i
    
    if(sum == x):
        return True
    
    return False

def main():
    a = int(input("Enter a number:"))

    if(perfect(a)):
        print("Perfect Number")
    
    else:
        print("Not a Perfect Number")

if __name__ == "__main__":
    main()