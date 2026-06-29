def square(value1):
    return value1*value1


def cube(value2):
    return value2*value2*value2


def main():
    no = int(input("Enter the no :"))
    Ret1 = square(no)
    print("Square is :",Ret1)

    Ret2 = cube(no)
    print("cube  is :",Ret2)


if __name__ == "__main__":
    main()