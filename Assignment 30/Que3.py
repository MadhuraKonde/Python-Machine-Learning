'''
Q3) Display File Line by Line

Problem Statement:
Write a program which accepts a file name from the user and displays the contents of the file line by line on the
screen.

Input:
Demo.txt

Expected Output:
Display each line of Demo. txt one by one.
'''

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

def printLines(file):
    if(not os.path.exists(file)):
        print(file,"does not exist !")
        return
    
    fobj = open(file,"r")

    '''
    while(True):
        line = fobj.readline()

        if(line == ""):
            break

        print(line,end="")
    '''
    
    for line in fobj:
        print(line,end="")

def main():
    file = input("Enter the file name :")

    printLines(file)

if __name__ == "__main__":
    main()