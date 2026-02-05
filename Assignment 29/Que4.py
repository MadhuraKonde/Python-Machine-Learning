'''
Q4) Compare Two Files (Command Line)

Problem Statement:
Write a program which accepts two file names through command line arguments and compares the contents of
both files.

-If both files contain the same contents, display Success
-Otherwise display Failure

Input (Command Line):
Demo.txt Hello.txt

Expected Output:
Success OR Failure
'''

import os
import sys

def compareFiles(file1,file2):
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
    fobj2 = open(file2,"r")

    data1 = fobj1.read()
    data2 = fobj2.read()

    fobj1.close()
    fobj2.close()

    if(data1 == data2):
        return 1
    
    return 0

def main():
    if(len(sys.argv) != 3):
        print("Number of arguments do not match !")
        return
    
    result = compareFiles(sys.argv[1],sys.argv[2])

    if(result):
        print("Success")
    
    elif(result == 0):
        print("Failure")

if __name__ == "__main__":
    main()