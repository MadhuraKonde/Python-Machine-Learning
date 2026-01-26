'''
Write a program which accept one number and display below pattern. 
Input : 5
Output : 
'''

def pattern(x):
    for i in range(1,x+1):
        for j in range(i):
            print(j+1,end="  ")
        
        print()

def main():
    a = int(input("Enter the number:"))

    pattern(a)

if __name__ == "__main__":
    main()