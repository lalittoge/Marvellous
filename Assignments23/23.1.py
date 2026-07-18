from multiprocessing import Pool
import os

def SumEven(n):
    total=0
    for i in range(2,n+1,2):
        total +=i
  

    print("process id is:",os.getpid())
    print("Given no is :",n)
    print("Sum of even no is :", total)


    return total

        

def main():
    Data = list(map(int,input("Enter the list elements:").split()))
    print(Data)

    with Pool() as p:
        result=p.map(SumEven,Data)

    print(result)

if __name__ == "__main__":
    main()