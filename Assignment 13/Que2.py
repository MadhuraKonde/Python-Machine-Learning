def circleArea(r):
    return (22/7)*r*r

def main():
    rad = int(input("Enter the radius of circle:"))

    cir_area = circleArea(rad)

    print("Area of circle:",cir_area)

if __name__ == "__main__":
    main()