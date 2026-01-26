import threading

lobj = threading.Lock()

def small(s):
    with lobj:
        print(f"Thread {threading.current_thread().name} started running with ID {threading.get_ident()}")
    
    scount = 0

    for i in s:
        if(ord(i) >= 97 and ord(i) <= 122):
            scount = scount + 1
    
    with lobj:
        print("Number of Lowercase characters :",scount)

def capital(s):
    with lobj:
        print(f"Thread {threading.current_thread().name} started running with ID {threading.get_ident()}")

    ccount = 0

    for i in s:
        if(ord(i) >= 65 and ord(i) <= 90):
            ccount = ccount + 1
    
    with lobj:
        print("Number of Uppercase characters :",ccount)

def digits(s):
    with lobj:
        print(f"Thread {threading.current_thread().name} started running with ID {threading.get_ident()}")

    dcount = 0

    for i in s:
        if(ord(i) >= 48 and ord(i) <= 57):
            dcount = dcount + 1
    
    with lobj:
        print("Number of Digits :",dcount)

def main():
    string = input("Enter a string : ")

    Small = threading.Thread(target=small , args=(string,))
    Capital = threading.Thread(target=capital , args=(string,))
    Digits = threading.Thread(target=digits , args=(string,))

    Small.start()
    Capital.start()
    Digits.start()

    Small.join()
    Capital.join()
    Digits.join()

if __name__ == "__main__":
    main()