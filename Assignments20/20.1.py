Square = lambda no : no * no
def main():
    no = int(input("Enter the no:"))

    Ret = Square(no)

    print(f"Square of the {no} is :{Ret}")

if __name__ == "__main__":
    main()