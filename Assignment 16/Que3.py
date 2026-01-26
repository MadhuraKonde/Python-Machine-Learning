def Add():
    print("Enter two numbers:")
    no1 = int(input())
    no2 = int(input())

    add = no1 + no2

    return add

def main():
    addition = Add()
    print("Addition :",addition)

if __name__ == "__main__":
    main()