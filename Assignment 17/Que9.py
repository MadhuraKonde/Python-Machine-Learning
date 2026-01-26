'''
Write a program which accept number from user and return number of digits in that number. 
Input : 5187934   
Output : 7
'''

def digitNo(x):
    n = 0

    while(x != 0):
        n = n + 1
        x = x//10
    
    return n

def main():
    a = int(input("Enter the number:"))

    d = digitNo(a)

    print("Number of digits :",d)

if __name__ == "__main__":
    main()