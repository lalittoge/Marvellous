from functools import reduce
import threading
import time

def Sum(Data):
    sum = 0

    for no in Data:
        sum = sum +no

    return sum

def Mul(Data):
    mul=1

    for no in Data:
        mul= mul*no

    return mul

    



def main():
    Data  = list(map(int,input("Enter the elements:").split()))
    start_time =time.perf_counter()

    Ret = Sum(Data)
    print(f"Sum of  no is {Ret}")
    
    Ret1 = Mul(Data)
    print(f"Mul of  no is {Ret1}")

    t1=threading.Thread(target=Sum,args=(Data,))
    t2=threading.Thread(target=Mul,args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()




    end_time =time.perf_counter()

    print(f"Total time is {end_time-start_time}")




if __name__ == "__main__":
    main()