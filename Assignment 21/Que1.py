import threading

lobj = threading.Lock()

def prime(l):
    plist = []

    for i in l:
        pflag = True

        for j in range(2,i//2+1):
            if(i % j == 0):
                pflag = False
                break
        
        if(pflag == True):
            plist.append(i)
    
    with lobj:
        print("Prime numbers :",plist)

def notprime(l):
    nplist = []

    for i in l:
        npflag = True

        for j in range(2,i//2+1):
            if(i % j == 0):
                npflag = False
                break
        
        if(npflag == False):
            nplist.append(i)
    
    with lobj:
        print("Not Prime numbers :",nplist)

def main():
    l = int(input("Enter the number of integers : "))

    integers = []

    print("Enter the integers :")
    for i in range(l):
        val = int(input())
        integers.append(val)
    
    print("Input List :",integers)

    Prime = threading.Thread(target=prime , args=(integers,))
    NotPrime = threading.Thread(target=notprime , args=(integers,))

    Prime.start()
    NotPrime.start()

    Prime.join()
    NotPrime.join()

if __name__ == "__main__":
    main()