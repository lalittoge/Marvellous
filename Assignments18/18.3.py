def Fact(no):
    fact = 1
    for i in range(1,no+1):
        fact=fact*i
    return fact

def main():
    no = int(input("Enter the no:"))
    Ret = Fact(no)

    print(f"Factorial of the {no} is {Ret}")

if __name__ == "__main__":
    main()