'''
Q2) Count Words in a File

Problem Statement:
Write a program which accepts a file name from the user and counts the total number of words in that file.

Input:
Demo.txt

Expected Output:
Total number of words in Demo.txt.
'''

import os

def countWords(file):
    if(not os.path.exists(file)):
        print(file,"does not exist !")
        return
    
    fobj = open(file,"r")

    n = 0
    '''
    c = fobj.read(1)
    while(c != ""):
        if(c == " " or c == "\n"):     #if " " at index 0?
            n += 1                     #if "\n" at the end of file

        c = fobj.read(1)

        n += 1                         # last word is not counted
    '''
    '''
    while(True):
        c = fobj.read(1)

        if(c == " " or c == "\n"):     #if " " at index 0?
            n += 1

        if(c == ""):
            fobj.seek(fobj.tell() - 1)
            c = fobj.read(1)

            if(c != "\n"):
                n += 1                 # last word is not counted
            break
    '''
    '''
    while(True):
        line = fobj.readline()

        if(line == ""):
            break

        words = line.split()
        n += len(words)
    '''
    
    for line in fobj:
        n += len(line.split()) 
    print(fobj.tell())
    
    return n

def main():
    file = input("Enter the file name :")

    wordno = countWords(file)

    if(wordno != None):
        print(f"Total Number of words in {file} are : {wordno}")

if __name__ == "__main__":
    main()