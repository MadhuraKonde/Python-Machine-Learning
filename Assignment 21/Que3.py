import threading

lobj = threading.Lock()

counter = 0

def update():
    global counter
    for i in range(100):
        with lobj:
            counter = counter + 1

def main():
    t1 = threading.Thread(target=update)
    t2 = threading.Thread(target=update)
    t3 = threading.Thread(target=update)
    t4 = threading.Thread(target=update)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    global counter
    print("Counter :",counter)

if __name__ == "__main__":
    main()