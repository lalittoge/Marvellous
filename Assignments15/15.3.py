Odd = lambda no : (no % 2 !=0)



def main():
    Data = list(map(int,input("Enter the list :").split()))

    FData = list(filter(Odd,Data))

    print("Data after filter is :",FData)


if __name__ == "__main__":
    main()