def Grade(x):
    if(x >= 75):
        print("Distinction")
    
    elif(x>=60):
        print("First Class")

    elif(x>=50):
        print("Second Class")
    
    else:
        print("Fail")

def main():
    marks = int(input("Enter your marks:"))

    Grade(marks)

if __name__ == "__main__":
    main()