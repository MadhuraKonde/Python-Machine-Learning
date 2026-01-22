def Sum(x):
    sum=0

    for i in range(1,x+1,1):
        sum = sum + i
    
    return sum

def main():
    a = int(input("Enter a number:"))

    sum = Sum(a)

    print(sum)

if __name__ == "__main__":
    main()