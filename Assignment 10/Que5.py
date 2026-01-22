def printOdd(x):
    for i in range(1,x+1,2):
        print(i,end=" ")

def main():
    a = int(input("Enter a number:"))

    printOdd(a)

if __name__ == "__main__":
    main()