Even = lambda val : val %  2 == 0


def main():
    no = int(input("Enter the no"))
    Ret = Even(no)

    print(Ret)

if __name__ == "__main__":
    main()