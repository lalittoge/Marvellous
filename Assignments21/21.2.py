import time
import threading

def FactEven(no):
    sum=0

    for i in range (2,no+1,2):
        if no % i==0:
            sum=sum+i

    print(sum)

def FactOdd(no):
    sum=0

    for i in range (1,no+1,2):
        if no % i==0:
            sum=sum+i

    print(sum)
        

def main():
    No=int(input("Enter the no:"))

    start_time=time.perf_counter()

    t1=threading.Thread(target=FactEven,args=(No,))
    t2=threading.Thread(target=FactOdd,args=(No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


    end_time=time.perf_counter()

    print(f"Time required is :{end_time-start_time:.04f}")

    print("Exit from main:")

    

if __name__ == "__main__":
    main()