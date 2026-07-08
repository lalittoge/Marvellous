def check(no):
    if no == 0:
        print("Zero")
    elif no >1:
        print("Positive")
    else:
        print("Negative")
def main():
    no = int(input("Enter the no:"))
    Ret = check(no)

if __name__ == "__main__":
    main()