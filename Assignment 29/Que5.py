'''
Q5) Frequency of a String in File

Problem Statement:
Write a program which accepts a file name and one string from the user and returns the frequency (count of
occurrences) of that string in the file.

Input:
Demo.txt Marvellous

Expected Output:
Count how many times "Marvellous" appears in Demo.txt.
'''

import os
import sys

def freqCounter(file,string):
    if(not os.path.exists(file)):
        print(f"{file} does not exist !")
        return
        
    fobj = open(file,"r")

    data = fobj.read()
    count = data.count(string)

    fobj.close()

    return count

def main():
    if(len(sys.argv) != 3):
        print("Number of arguments do not match !")
        return
    
    count = freqCounter(sys.argv[1],sys.argv[2])

    print(f"{sys.argv[2]} appears {count} times in {sys.argv[1]}")


if __name__ == "__main__":
    main()