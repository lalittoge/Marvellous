import sys

def Add():
    No1 = int(sys.argv[1])
    No2 = int(sys.argv[2])

    return No1+No2

def main():
    Ret = Add()

    print(f"Addition is {Ret}")

if __name__ == "__main__":
    main()