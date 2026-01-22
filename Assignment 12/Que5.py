def ReverseSequence(x):
    for i in range(x,0,-1):
        print(i,end=" ")

def main():
    a = int(input("Enter a number:"))

    ReverseSequence(a)

if __name__ == "__main__":
    main()