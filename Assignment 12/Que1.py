def checkVowel(x):
    if(x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
        return True
    
    return False

def main():
    a = input("Enter a letter:")

    a_ascii = ord(a)

    if((a_ascii>=65 and a_ascii<=90) or (a_ascii>=97 and a_ascii<=122)):
        if(checkVowel(a)):
            print("Vowel")
        
        else:
            print("Consonant")
    
    else:
        print("Entered character is not a Letter!")


if __name__ == "__main__":
    main()