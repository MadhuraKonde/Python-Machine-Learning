'''
def even10():
    i = 1
    n = 2
    while(i <= 10):
        print(n,end="\t")
        n = n + 2
        i = i + 1
'''

def even10():
    i = 1
    while(i <= 10):
        print(i*2,end="\t")
        i = i + 1

def main():
    even10()

if __name__ == "__main__":
    main()