'''
def length(s):
    l = 0

    while(s != ""):
        l = l + 1
        s = s[1:]
    
    return l
'''

def length(s):
    l = 0

    for i in s:
        l = l + 1
    
    return l

def main():
    name = input("Enter a string : ")

    len = length(name)

    print(len)

if __name__ == "__main__":
    main()