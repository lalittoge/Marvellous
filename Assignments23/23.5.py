from multiprocessing import Pool
import os

def Factorial(n):
    Fact=1
    for i in range(1,n+1):
        Fact= Fact * i
  

    print("process id is:",os.getpid())
    print("Given no is :",n)
    print("Factorial of no is :", Fact)


    return Fact

        

def main():
    Data = list(map(int,input("Enter the list elements:").split()))
    print(Data)

    with Pool() as p:
        result=p.map(Factorial,Data)

    print(result)

if __name__ == "__main__":
    main()