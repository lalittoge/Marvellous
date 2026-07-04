Divide5 = lambda val : val % 5 ==0

def main():
    no = int(input("Enter the no:"))
    
    Ret = Divide5(no)

    print(Ret)


if __name__ == "__main__":
    main()