def main():
    no = int(input("Enter the no"))
    reverse = 0
    while no > 0:
        digit = no % 10
        reverse = reverse * 10 + digit
        no = no // 10
    print("reverse of no is:", reverse)



if __name__ == "__main__":
    main()