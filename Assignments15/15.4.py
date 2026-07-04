from functools import reduce

Add = lambda no1, no2 :no1+no2


def main():
    Data = list(map(int,input("Enter the list:").split()))

    RData =reduce(Add,Data)

    print("Addition of of all list:",RData)


if __name__ == "__main__":
    main()