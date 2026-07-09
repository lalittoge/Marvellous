def main():
    no = int(input("Enter the no"))
    if no == 0:
        print("no of digit is :",1)
    count = 0
    while no > 0:
        count = count +1
        no = no // 10
    print("no of digit is :",count)


if __name__ == "__main__":
    main()