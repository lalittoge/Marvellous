Len = lambda s : len(s)>5 

def main():
    List = input("Enter the string:").split()
    print(List)

    FList = list(filter(Len,List))

    print("Final list:",FList)
if __name__ == "__main__":
    main()