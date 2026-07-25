from multiprocessing import Pool
def CountPrime(Data):
    for i in range(Data):
        print 
    




def main():

    Data = list(map(int,input("Enter the list :").split()))
    print(Data)

    with Pool as p:
        result=p.map(CountPrime,Data)
    
    print(result)




if __name__ == "__main__":
    main()