MaxNum = lambda Value1,Value2: Value1 > Value2
    

def main():
    no1 = int(input("Enter the first number:"))
    no2 = int(input("Enter the second number"))

    Ret = MaxNum(no1,no2)
    if Ret:
        print("Max of the no is ",no1)
    else:
        print("Max of the no is ",no2)





if __name__ == "__main__":
    main()
