'''
Write a program which accept one number and display below pattern. 
Input : 5
Output : *  *  *  *  *
         *  *  *  *
         *  *  *
         *  *
         *
'''

'''
def pattern(x):
    for i in range(x):
        for j in range(x-i,0,-1):
            print("*",end="  ")
        
        print()
'''
'''
def pattern(x):
    for i in range(x):
        for j in range(0,x-i):
            print("*",end="  ")
        
        print()
'''

def pattern(x):
    for i in range(x,0,-1):
        for j in range(i):
            print("*",end="  ")
        
        print()

def main():
    a = int(input("Enter the number:"))

    pattern(a)

if __name__ == "__main__":
    main()