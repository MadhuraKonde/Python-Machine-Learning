'''
Write a program which accept one number for user and check whether number is prime or not. 
Input : 5
Output : It is Prime Number
'''

def checkPrime(x):
    if(x <= 1):
        return False
    
    for i in range(2,x//2+1):
        if(x % i == 0):
            return False
    
    return True

def main():
    a = int(input("Enter the number : "))

    if(checkPrime(a)):
        print("It is a Prime Number!")
    
    else:
        print("It is not a Prime Number!")

if __name__ == "__main__":
    main()