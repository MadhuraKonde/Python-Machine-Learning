def Factors(x):
    print("1",end=" ")

    for i in range(2,(x//2)+1,1):
        if(x % i == 0):
            print(i,end=" ")
    
    print(x)

def main():
    a = int(input("Enter a number:"))

    Factors(a)

if __name__ == "__main__":
    main()