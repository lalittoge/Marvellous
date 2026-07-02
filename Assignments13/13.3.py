def main():
    no = int(input("Enter the number :"))
    s =""
    while (no>0):
        r = no %2
        s = str(r)+s
        no = no//2

    print(int(s))



if __name__ == "__main__":
    main()