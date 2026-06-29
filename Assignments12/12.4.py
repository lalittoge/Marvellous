def divide(no):
    if no % 3 == 0 and no % 5 == 0:
        print("no is divisible by 3 and 5")
    else:

        print("no is not divisible by 3 and 5")
    


def main():
    no = int(input("Enter the no:"))
    divide(no)


if __name__ =="__main__":
    main()
