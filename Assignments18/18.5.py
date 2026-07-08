def Prime(no):
    if no <= 1:
        print("Not Prime")
        return

    for i in range(2, no):
        if no % i == 0:
            print("Not Prime")
            return

    print("Prime")

def main():
    no = int(input("enter the no:"))
    Prime(no)


if __name__ == "__main__":
    main()