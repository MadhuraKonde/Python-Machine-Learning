import threading

def print50():
    for i in range(1,51):
        print(i)

def reverse50():
    for i in range(50,0,-1):
        print(i)

def main():
    Thread1 = threading.Thread(target=print50)
    Thread2 = threading.Thread(target=reverse50)

    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()