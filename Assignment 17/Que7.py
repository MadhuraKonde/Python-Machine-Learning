'''
Write a program which accept one number and display below pattern. 
Input : 5
Output : 1  2  3  4  5
         1  2  3  4  5
         1  2  3  4  5
         1  2  3  4  5
         1  2  3  4  5
'''
def pattern(x):
    for i in range(x):
        for j in range(x):
            print(j+1,end="  ")
        
        print()

def main():
    a = int(input("Enter the number:"))

    pattern(a)

if __name__ == "__main__":
    main()