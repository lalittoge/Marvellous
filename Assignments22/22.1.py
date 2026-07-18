from multiprocessing import Pool
def square(Data):
    return [i*i for i in range(1,Data+1)]
    
def main():
    Data = list(map(int,input("Enter  the list:").split()))
    print(Data)

    with Pool() as p:
        result=p.map(square,Data)

    print(result)

    

   

if __name__ == "__main__":
    main()