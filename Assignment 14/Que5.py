checkEven = lambda x : x % 2 == 0

def main():
    a = int(input("Enter a number:"))

    if(checkEven(a)):
        print(a,"is Even!")
    
    else:
        print(a,"is not Even!")

if __name__ == "__main__":
    main()