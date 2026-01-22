def table(x):
    for i in range(1,11,1):
        print(x*i,end=" ")

def main():
    a = int(input("Enter a number:"))

    table(a)

if __name__ == "__main__":
    main()