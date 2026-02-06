'''
Q5) Search a Word in File

Problem Statement:
Write a program which accepts a file name and a word from the user and checks whether that word is present in
the file or not.

Input:
Demo.txt Marvellous

Expected Output:
Display whether the word Marvellous is found in Demo. txt or not.
'''

import os

def wordSearch(file,word):
    if(not os.path.exists(file)):
        print(file,"does not exist !")
        return
    
    fobj = open(file,"r")

    data = fobj.read()

    if word in data:
        print(f"{word} is found in {file}")
    
    else:
        print(f"{word} is not found in {file}")

def main():
    file = input("Enter the file name :")
    word = input("Enter the word to check :")

    wordSearch(file,word)

if __name__ == "__main__":
    main()