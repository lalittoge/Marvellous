#Took N list find add of prime no from it

from MarvellousNum import ChkPrime

def add (List):
    Sum = 0
    for no in List:
        Sum = Sum + no
    return Sum


def main():
    no = int(input("Enter the no ofelemets"))
    Data = []
    for i in range (no):
        val = int(input("enter the elemts "))
        Data.append(val)
    
        
    print(f"List is {Data}")

    Ret = ChkPrime(Data)

    print(f"Prime list is : {Ret}")

    Add = add(Ret)

    print(f"Sum of prime no is :{Add}")


if __name__ =="__main__":
    main()