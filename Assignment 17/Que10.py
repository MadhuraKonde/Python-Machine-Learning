'''
Write a program which accept number from user and return addition of digits in that number. 
Input : 5187934   
Output : 37
'''

def digitAdd(x):
    add = 0

    while(x != 0):
        d = x % 10
        add = add + d
        x = x//10
    
    return add

def main():
    a = int(input("Enter the number:"))

    dadd = digitAdd(a)

    print("Addition of digits :",dadd)

if __name__ == "__main__":
    main()