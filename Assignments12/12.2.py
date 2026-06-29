def ChkGreater(Value1,Value2):
    if Value1 > Value2:
        print("Greater no is :", Value1)
    else:
        print("Greater no is :", Value2)




def main():
    no1= int(input("Enter the first no:"))
    no2 = int(input("Enter the second no:"))

    ChkGreater(no1,no2)

if __name__ == "__main__":
    main()
