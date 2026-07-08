# took list of N no add also took no to be find and its occurance

def main():
    no = int(input("Enter the no of elemets in list"))
    Data = []
    
    for i in range(no):
        val = int(input("Enter the elements in list:"))
        Data.append(val)
    print(f"List is : {Data}")


    search= int(input("Enter no to be search:"))
    counter = 0

    for i in Data:
        if i == search:
            counter +=1
    print(f" the occurance of {search} is {counter}")


        

if __name__ =="__main__":
    main()