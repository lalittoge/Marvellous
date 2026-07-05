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
    EvenSum(10000000)
    OddSum(100000000)

if __name__ == "__main__":
    main()

