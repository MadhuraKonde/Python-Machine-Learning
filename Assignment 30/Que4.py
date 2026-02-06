'''
Q4) Copy File Contents into Another File

Problem Statement:
Write a program which accepts two file names from the user.

. First file is an existing file

. Second file is a new file

Copy all contents from the first file into the second file.

Contents of ABC. txt copied into Demo. txt.
'''

import os
import sys

def CopyContents(file1,file2):
    if(not os.path.exists(file1)):
        print(f"{file1} does not exist !")
        if(not os.path.exists(file2)):
            print(f"{file2} does not exist !")
        return
    
    if(os.path.exists(file1)):
        if(not os.path.exists(file2)):
            print(f"{file2} does not exist !")
            return
    
    
    fobj1 = open(file1,"r")
    fobj2 = open(file2,"w")

    data = fobj1.read()
    fobj2.write(data)

    print("Copied Content is :")
    print(data)

    fobj1.close()
    fobj2.close()

def main():
    file1 = input("Enter the first file name :")
    file2 = input("Enter the second file name :")

    CopyContents(file1,file2)

if __name__ == "__main__":
    main()