'''
Q3) Copy File Contents into a New File (Command Line)

Problem Statement:
Write a program which accepts an existing file name through command line arguments, creates a new file
named Demo. txt, and copies all contents from the given file into Demo. txt.

Input (Command Line):
ABC.txt

Expected Output:
Create Demo. txt and copy contents of ABC. txt into Demo.txt.
'''

import os
import sys

def CopyContents(file):
    if(not os.path.exists(file)):
        print("File does not exist !")
        return
    
    else:
        fobj1 = open(file,"r")
        fobj2 = open("Demo.txt","w")

        data = fobj1.read()
        fobj2.write(data)

def main():
    if(len(sys.argv) != 2):
        print("Number of arguments do not match !")
        return
    
    print(f"Copying content of {sys.argv[1]} into Demo.txt")
    CopyContents(sys.argv[1])
    print("Content Copied successfully !")

if __name__ == "__main__":
    main()