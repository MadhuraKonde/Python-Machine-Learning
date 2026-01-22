def rectangleArea(l,b):
    return l*b

def main():
    len = int(input("Enter the length of rectangle:"))
    wt = int(input("Enter the width of rectangle:"))

    rec_area = rectangleArea(len,wt)

    print("Area of Rectangle:",rec_area)

if __name__ == "__main__":
    main()