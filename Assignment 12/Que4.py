def Sequence(x):
    for i in range(1,x+1,1):
        print(i,end=" ")

def main():
    a = int(input("Enter a number:"))

    Sequence(a)

if __name__ == "__main__":
    main()