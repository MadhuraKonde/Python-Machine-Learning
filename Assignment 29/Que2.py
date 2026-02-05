'''
Q2) Display File Contents

Problem Statement:
Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the
console.

Input:
Demo.txt

Expected Output:
Display contents of Demo. txt on console.
'''

import os

def DisplayContent(file):
    if(not os.path.exists(file)):
       print("File does not exist !")
       return
    
    fobj = open(file,"r")

    data = fobj.read()

    print(data)

    fobj.close()

def main():
    file = input("Enter file name : ")

    print(f"Displaying Contents of the file {file} :")
    DisplayContent(file)

if __name__ == "__main__":
    main()