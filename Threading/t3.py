import time
import threading

def EvenSum(No):
    Sum = 0
    for i in range(2,No,2):
        Sum= Sum+i
    print("Sum of even no is :", Sum)


def OddSum(No):
    Sum = 0
    for i in range(1,No,2):
        Sum= Sum+i
    print("Sum of odd no is :", Sum)

def main():

    start_time = time.perf_counter()

    t1= threading.Thread(target=EvenSum,args=(10000000,))
    t2 = threading.Thread(target=OddSum,args=(100000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()

    print(f"Time required for execution is : {end_time-start_time:.5f}")

if __name__ == "__main__":
    main()

