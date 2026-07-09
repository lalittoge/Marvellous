# Enter N elements in list and find max no

from functools import reduce
Max = lambda No1, No2 : No1 if No1 >No2 else No2


def main():
    No = int(input("Enter the no of elements in list :"))
    Data = []
    for i in range(No):
        val = int (input("Enter the list:"))
        Data.append(val)

    RData = reduce(Max, Data)

    print(f"Max no is {RData} ")

    print(f"List is : {Data}")



        

if __name__ =="__main__":
    main()