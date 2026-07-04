Min = lambda Value1,Value2: Value1 < Value2

def main():
    no1 = int(input("Enter the first no :"))

    no2 = int(input("Enter the second no :"))

    Ret = Min(no1,no2)

    if (Ret == True):
        print("Minium no is :", no1)
    else:
        print("Minium no is :", no2)

if __name__ == "__main__":
    main()