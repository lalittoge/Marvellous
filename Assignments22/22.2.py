from multiprocessing import Pool
def square(Data):
    Fact=1
    for i in range(1,Data+1):
        Fact=i*Fact

    return Fact

    
def main():
    Data = list(map(int,input("Enter  the list:").split()))
    print(Data)

    with Pool() as p:
        result=p.map(square,Data)

    print(result)

    

   

if __name__ == "__main__":
    main()