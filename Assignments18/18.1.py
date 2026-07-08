from Arithmatic import *


def main():
    No1 = int(input("Enter the first no:"))
    No2 = int(input("Enter the second no:"))
    Ret1 = add(No1,No2)
    print("Addition is :", Ret1)

    Ret2 = sub(No1,No2)
    print("sub is :", Ret2)

    Ret3 = mul(No1,No2)
    print("mul is :", Ret3)

    Ret4 = div(No1,No2)
    print("divide is :", Ret4)



if __name__ == "__main__":
    main()