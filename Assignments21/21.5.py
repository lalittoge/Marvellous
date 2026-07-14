import time
import threading

def Thread1(no):
    for i in range(1,no+1):
        print(i)


def Thread2(no):
    for i in range(no,0,-1):
        print(i)


def main():

    start_time = time.perf_counter()


    no = 50

    t1=threading.Thread(target=Thread1,args=(no,))
    
    t2=threading.Thread(target=Thread2,args=(no,))

    t1.start()
    t1.join()


    t2.start()
    t2.join()


    end_time = time.perf_counter()

    print(f"Time need is :{end_time-start_time:0.4f}")
if __name__ == "__main__":
    main()