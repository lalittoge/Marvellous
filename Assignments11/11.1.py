def main():
    no = int(input("Enter the no :"))
    if no <= 1:
        print("not prime")
    else:
        for i in range(2,no+1):
            if(no%i!=0):

                print("no is  prime")
                break
            else:
                print("not prime")

if __name__ == "__main__":
    main()