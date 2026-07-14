import time
import threading


def SumEven(List):
    sum=0
    for i in List:
        if i%2==0:
            sum=sum+i
    print(sum)

def SumOdd(List):
    sum=0
    for i in List:
        if i%2!=0:
            sum=sum+i
    print(sum)


def main():
    Data = list(map(int,input("Enter the elemets :").split()))
    print(Data)

    start_time= time.perf_counter()

    t1=threading.Thread(target=SumEven,args=(Data,))
    t2=threading.Thread(target=SumOdd,args=(Data,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    


    end_time= time.perf_counter()

    print(f"Time Required is :{end_time-start_time:.4f}")

if __name__ == "__main__":
    main()