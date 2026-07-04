from functools  import reduce

Min = lambda no1 ,no2 : no1 if no1 < no2 else no2

def main():
    Data = list(map(int, input("Enter the list:").split()))

    RData = reduce(Min,Data)

    print("Min of the no of list is :",RData)

if __name__ == "__main__":
    main()