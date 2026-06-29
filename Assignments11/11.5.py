def main():
    no = int(input("Enter the no :"))
    reverse = 0
    org = no
    while no > 0:
        digit = no % 10
        reverse = reverse * 10 + digit
        no = no //10
    if org == reverse:
        print("no is pllindrome")
    else:
        print("no is not pallindrome"
        "")


if __name__=="__main__":
    main()