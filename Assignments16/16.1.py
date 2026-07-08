def main():
    No = int(input("Enter the no of elements in list :"))
    Data = []
    for i in range(No):
        val = int (input("Enter the list:"))
        Data.append(val)

    print(f"List is : {Data}")
        

if __name__ =="__main__":
    main()

