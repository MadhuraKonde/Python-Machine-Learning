'''
Write a program which accept one number and display below pattern. 
Input : 5
Output: *  *  *  *  *  
        *  *  *  *  *  
        *  *  *  *  *  
        *  *  *  *  *  
        *  *  *  *  *
'''
def pattern(x):
    for i in range(x):
        for j in range(x):
            print("*",end="  ")
        
        print()

def main():
    a = int(input("Enter the number:"))

    pattern(a)

if __name__ == "__main__":
    main()