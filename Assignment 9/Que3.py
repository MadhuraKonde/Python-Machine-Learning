def square(x):
    sq = x*x
    return sq

def main():
    a = int(input("Enter a number:"))

    sq = square(a)

    print(sq)

if __name__ == "__main__":
    main()