def Area(Value1 , Value2):
    return Value1 * Value2
def main():
    no1 = int(input("Eneter the first no :"))
    no2 = int(input("Enter the second  no :"))
    area = Area(no1,no2)
    print("Area of the rectangle ", area)

if __name__ == "__main__":
    main()