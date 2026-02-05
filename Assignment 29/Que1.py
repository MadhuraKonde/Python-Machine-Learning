'''
Q1) Check File Exists in Current Directory

Problem Statement:
Write a program which accepts a file name from the user and checks whether that file exists in the current
directory or not.

Input:
Demo.txt

Expected Output:
Display whether Demo. txt exists or not.
'''

import os

def main():
    file = input("Enter file name : ")

    if(os.path.exists(file)):
        print(file,"exists ! ")
    
    else:
        print(file,"does not exist !")

if __name__ == "__main__":
    main()