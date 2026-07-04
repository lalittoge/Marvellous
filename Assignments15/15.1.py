Square = lambda no : no*no

def main():
    Data = list(map(int,input("Enter the list ").split()))
    print(Data)



    Fdata = list(map(Square,Data))

    print("Data after filte:",Fdata)


if __name__ == "__main__":
    main()

