import threading
import time

def Prime(data):
    print("Prime numbers:")
    for no in data:
        if no > 1:
            for i in range(2, no):
                if no % i == 0:
                    break
            else:
                print(no, end=" ")
    print()


def NonPrime(data):
    print("Non-Prime numbers:")
    for no in data:
        if no <= 1:
            print(no, end=" ")
        else:
            for i in range(2, no):
                if no % i == 0:
                    print(no, end=" ")
                    break
    print()


def main():
    data = list(map(int, input("Enter numbers: ").split()))


    start_time = time.perf_counter()

    t1 = threading.Thread(target=Prime,args=(data,))
    t2 = threading.Thread(target=NonPrime,args=(data,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    end_time = time.perf_counter()

    print(f"Time required is : {end_time-start_time:.4f}")
    


if __name__ == "__main__":
    main()