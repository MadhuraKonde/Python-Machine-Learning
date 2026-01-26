def pattern(x):
    for i in range(x):
        print("*",end="\t")

def main():
    a = int(input("Enter the number of * :"))
    pattern(a)

if __name__ == "__main__":
    main()