from functools  import reduce

Max = lambda no1 ,no2 : no1 if no1 > no2 else no2

def main():
    Data = list(map(int, input("Enter the list:").split()))

    RData = reduce(Max,Data)

    print("Max of the no of list is :",RData)

if __name__ == "__main__":
    main()