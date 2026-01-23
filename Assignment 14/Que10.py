#greater3 = lambda x,y,z : max(x,y,z)
#greater3 = lambda x,y,z : x if (x>y and x>z) else greater3(y,z,x)
greater3 = lambda x,y,z : x if (x>y and x>z) else (y if y>z else z)

def main():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    c = int(input("Enter third number:"))

    gr = greater3(a,b,c)

    print("Largest number :",gr)

if __name__ == "__main__":
    main()