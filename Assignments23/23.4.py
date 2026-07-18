from multiprocessing import Pool
import os

def SumOdd(n):
    count=0
    for i in range(1,n+1,2):
        count +=1
  

    print("process id is:",os.getpid())
    print("Given no is :",n)
    print("count of odd no is :", count)


    return count

        

def main():
    Data = list(map(int,input("Enter the list elements:").split()))
    print(Data)

    with Pool() as p:
        result=p.map(SumOdd,Data)

    print(result)

if __name__ == "__main__":
    main()