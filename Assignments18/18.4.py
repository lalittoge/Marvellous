def Fact(no):
    sum=0 
    for i in range(1,no):
        if no%i==0:
            sum =sum+i
    return sum

def main():
    no = int(input("Enter the no:"))
    Ret = Fact(no)

    print(f"add of fact of the {no} is {Ret}")

if __name__ == "__main__":
    main()