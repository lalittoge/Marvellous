Max= lambda a, b, c: a if (a >= b and a >= c) else (b if b >= c else c)

def main():
    no1 = int(input("Enter the first no :"))
    no2 = int(input("Enter the first no :"))
    no3 = int(input("Enter the first no :"))

    Ret = Max(no1, no2, no3)
    print("Maximum number is:", Ret)



if __name__ == "__main__":
    main()

