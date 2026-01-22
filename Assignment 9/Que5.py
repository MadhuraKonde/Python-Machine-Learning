def div3(x):
    if (x % 3 == 0):
        return True
    
    else:
        return False

def div5(x):
    if (x % 5 == 0):
        return True
    
    else:
        return False

def main():
    a = int(input("Enter a number:"))

    if(div3(a) and div5(a)):
        print("Divisible by 3 and 5")
    
    else:
        print("Not divisible by 3 and 5")

if __name__ == "__main__":
    main()