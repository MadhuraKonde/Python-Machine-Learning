'''
Q1) Count Lines in a File

Problem Statement:
Write a program which accepts a file name from the user and counts how many lines are present in the file.

Input:
Demo.txt

Expected Output:
Total number of lines in Demo. txt.
'''

import os

def countLines(file):
    if(not os.path.exists(file)):
        print(file,"does not exist !")
        return
    
    fobj = open(file,"r")

    n = 0
    oc = ""
    '''
    while(True):
        line = fobj.readline()

        if(line == ""):
            break

        n += 1
    '''

    while(True):
        c = fobj.read(1)

        if(c == ""):
            if(oc != "\n"):
                n += 1
            break

        if(c == "\n"):
            n += 1

        oc = c
        
    return n


def main():
    file = input("Enter the file name :")

    lineno = countLines(file)

    if(lineno != None):
        print(f"Total Number of lines in {file} are : {lineno}")

if __name__ == "__main__":
    main()