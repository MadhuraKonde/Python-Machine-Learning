#greater = lambda x,y : max(x,y)
greater = lambda x,y : x if (x>y) else y

def main():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))

    gr = greater(a,b)

    print("Greater number is :",gr)

if __name__ == "__main__":
    main()