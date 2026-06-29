def main():
    no = int(input("Enter the no"))
    total = 0
    while no > 0:
        digit = no % 10
        total = total + digit
        no = no // 10
    print("sum is :",total)


if __name__ == "__main__":
    main()