def ChkGreater(x,y):
    if (x > y):
        print(x,"is greater")
    
    else:
        print(y,"is greater")

def main():
    print("Enter two numbers:")
    a=int(input())
    b=int(input())

    ChkGreater(a,b)

if __name__ == "__main__":
    main()