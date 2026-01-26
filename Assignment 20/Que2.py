import threading

lobj=threading.Lock()

def EvenFactorSum(x):
    sum = 0

    for i in range(2,x//2+1):
        if(x % i == 0):
            if(i % 2 == 0):
                sum = sum + i
    
    with lobj:
        print("Sum of Even Factors :",sum)

def OddFactorSum(x):
    sum = 0

    for i in range(2,x//2+1):
        if(x % i == 0):
            if(i % 2 == 1):
                sum = sum + i
    
    with lobj:
        print("Sum of Odd Factors :",sum)

def main():
    n = int(input("Enter a number : "))

    EvenFactor = threading.Thread(target=EvenFactorSum , args=(n,))
    OddFactor = threading.Thread(target=OddFactorSum , args=(n,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("Exit from main")

if __name__ == "__main__":
    main()