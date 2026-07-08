# Enter N elements in list and find min no

from functools import reduce
Min = lambda No1, No2 : No1 if No1 < No2 else No2


def main():
    No = int(input("Enter the no of elements in list :"))
    Data = []
    for i in range(No):
        val = int (input("Enter the list:"))
        Data.append(val)

    RData = reduce(Min, Data)

    print(f"Min no is {RData} ")

   



        

if __name__ =="__main__":
    main()