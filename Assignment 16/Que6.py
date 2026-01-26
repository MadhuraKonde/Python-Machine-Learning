def checkNumber(x):
    if(x > 0):
        print("Positive Number")
    
    elif(x < 0):
        print("Negative Number")
    
    else:
        print("Zero")

def main():
    a = int(input("Enter a number:"))
    checkNumber(a)

if __name__ == "__main__":
    main()