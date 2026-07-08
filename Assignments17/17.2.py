import sys

def ChkNum():
    No1 = int(sys.argv[1])
    if No1 % 2== 0:
        print("Even ")
    else:
        print("Odd")


def main():
    
    ChkNum()


if __name__ == "__main__":
    main()