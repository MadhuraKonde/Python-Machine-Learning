checkOdd = lambda x : x % 2 == 1

def main():
    a = int(input("Enter a number:"))

    if(checkOdd(a)):
        print(a,"is Odd!")
    
    else:
        print(a,"is not Odd!")

if __name__ == "__main__":
    main()