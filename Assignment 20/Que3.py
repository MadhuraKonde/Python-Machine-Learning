import threading

lobj=threading.Lock()

def EvenListSum(x):
    sum = 0

    for i in x:
        if(i % 2 == 0):
            sum = sum + i
    
    with lobj:
        print("Sum of Even Elements :",sum)

def OddListSum(x):
    sum = 0

    for i in x:
        if(i % 2 == 1):
            sum = sum + i
    
    with lobj:
        print("Sum of Odd Elements :",sum)

def main():
    l = int(input("Enter the number of elements : "))

    numbers = []

    print("Enter the elements :")
    for i in range(l):
        val = int(input())
        numbers.append(val)
    
    print("Input List :",numbers)

    EvenList = threading.Thread(target=EvenListSum , args=(numbers,))
    OddList = threading.Thread(target=OddListSum , args=(numbers,))

    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join()

    print("Exit from main")

if __name__ == "__main__":
    main()