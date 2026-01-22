def printEven(x):
    for i in range(2,x+1,2):
        print(i,end=" ")

def main():
    a = int(input("Enter a number:"))

    printEven(a)

if __name__ == "__main__":
    main()