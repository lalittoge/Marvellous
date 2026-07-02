def perfectNo(Value):
    sum = 0
    for i in range(1,Value):
        if (Value % i == 0):
            sum = sum + i
    if sum==Value:
        return True
    else:
        False


def main():
    no = int(input("Enter the given no:"))
    Ret = perfectNo(no)

    if Ret ==True:
        print("No is prime")
    else:
        print("No is not prime")

if __name__ == "__main__":
    main()