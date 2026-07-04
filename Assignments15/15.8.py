def main():
    Data = list(map(int,input("Enter the list").split()))
    FData = list(filter((lambda no: no %3 ==0 and no% 5==0),Data))

    print("No divisible by 3 and 5 are :",FData)

if __name__ == "_main__":
    main()