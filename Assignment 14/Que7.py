divisible5 = lambda x : x % 5 == 0

def main():
    a = int(input("Enter a number:"))

    if(divisible5(a)):
        print(a,"is divisible by 5!")
    
    else:
        print(a,"is not divisible by 5!")

if __name__ == "__main__":
    main()