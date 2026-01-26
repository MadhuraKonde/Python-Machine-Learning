import threading

lobj=threading.Lock()

def even():
    with lobj:
        print("First 10 even numbers :")
        for i in range(0,10):
            print(i*2)

def odd():
    with lobj:
        print("First 10 odd numbers :")
        for i in range(0,10):
            print(i*2 + 1)

def main():
    Even = threading.Thread(target=even)
    Odd = threading.Thread(target=odd)

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

if __name__ == "__main__":
    main()