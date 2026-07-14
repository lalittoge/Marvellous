from functools import reduce
import threading
import time

def Max(Data):
    maximum = Data[0]

    for no in Data:
        if no > maximum:
            maximum = no

    return maximum

def Min(Data):
    minimum = Data[0]

    for no in Data:
        if no < minimum:
            minimum = no

    return minimum

    



def main():
    Data  = list(map(int,input("Enter the elements:").split()))
    start_time =time.perf_counter()

    Ret = Max(Data)
    print(f"Max no is {Ret}")
    
    Ret1 = Min(Data)
    print(f"Max no is {Ret1}")

    t1=threading.Thread(target=Max,args=(Data,))
    t2=threading.Thread(target=Min,args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()




    end_time =time.perf_counter()

    print(f"Total time is {end_time-start_time}")




if __name__ == "__main__":
    main()