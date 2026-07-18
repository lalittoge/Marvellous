from multiprocessing import Pool
import os

def SumEven(n):
    count=0
    for i in range(2,n+1,2):
        count +=1
  

    print("process id is:",os.getpid())
    print("Given no is :",n)
    print("count of even no is :", count)


    return count

        

def main():
    Data = list(map(int,input("Enter the list elements:").split()))
    print(Data)

    with Pool() as p:
        result=p.map(SumEven,Data)

    print(result)

if __name__ == "__main__":
    main()