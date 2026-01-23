strlength5 = lambda s : len(s)>5

def main():
    l = int(input("Enter the number of strings:"))

    strings = []

    print("Enter the strings:")
    for i in range(l):
        val = input()
        strings.append(val)
    
    print("Strings :",strings)
    
    lengthList = list(filter(strlength5,strings))

    print("Strings having length greater than 5 :",lengthList)

if __name__ == "__main__":
    main()