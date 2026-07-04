Even = lambda no : no %2 == 0


def main():
    Data = list(map(int,input("Enter the list :").split()))

    FData = list(filter(Even,Data))
    Count= len(FData)

    print("Even no are :", FData)
    print("Count of even no is",Count)

if __name__ == "__main__":
    main()