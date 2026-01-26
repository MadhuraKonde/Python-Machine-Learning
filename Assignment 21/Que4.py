import threading

sum = 0
def sumList(l):
    global sum

    for i in l:
        sum = sum + i

mul = 1
def proList(l):
    global mul

    for i in l:
        mul = mul * i

def main():
    l = int(input("Enter the number of integers : "))

    integers = []

    print("Enter the integers :")
    for i in range(l):
        val = int(input())
        integers.append(val)
    
    print("Input List :",integers)

    t1 = threading.Thread(target=sumList , args=(integers,))
    t2 = threading.Thread(target=proList , args=(integers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements in list :",sum)
    print("Product of elements in list :",mul)

if __name__ == "__main__":
    main()