'''
Write a program which accept one number form user and return addition of its factors.
Input : 12
Output : 16
'''

def factorAdd(x):
    sum = 1

    for i in range(2,x//2+1):
        if(x % i == 0):
            sum = sum + i
    
    return sum

def main():
    a = int(input("Enter the number : "))

    fadd = factorAdd(a)

    print("Addition of factors :",fadd)

if __name__ == "__main__":
    main()