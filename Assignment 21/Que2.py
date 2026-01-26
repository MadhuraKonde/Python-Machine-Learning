import threading

lobj = threading.Lock()

def maxList(l):
    max = l[0]

    for i in l:
        if(i > max):
            max = i
    
    with lobj:
        print("Maximum element from list :",max)

def minList(l):
    min = l[0]

    for i in l:
        if(i < min):
            min = i

    with lobj:
        print("Minimum element from list :",min)

def main():
    l = int(input("Enter the number of integers : "))

    integers = []

    print("Enter the integers :")
    for i in range(l):
        val = int(input())
        integers.append(val)
    
    print("Input List :",integers)

    t1 = threading.Thread(target=maxList , args=(integers,))
    t2 = threading.Thread(target=minList , args=(integers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()