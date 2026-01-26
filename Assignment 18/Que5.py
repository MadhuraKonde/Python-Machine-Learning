from MarvellousNum import Chkprime

def ListPrime(l):
    sum = 0

    for i in l:
        if(Chkprime(i)):
            sum = sum + i
    
    return sum

def main():
    n = int(input("Number of elements : "))

    numbers = []

    print("Input Elements :")
    for i in range(n):
        val = int(input())
        numbers.append(val)

    padd = ListPrime(numbers)

    print("Addition of prime numbers :",padd)

if __name__ == "__main__":
    main()