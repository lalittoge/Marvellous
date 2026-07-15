class Numbers:
    def __init__(self):
        self.Value=int(input("Enter the number:"))
        

    def ChkPrime(self):
        for i in range(2,self.Value):
            if self.Value % i!=0:
                print("True")
                break
            else:
                print("False")
                break

    def Factor(self):
        for i in range(2,self.Value):
            if self.Value %i==0:
                print(i)


    def SumFactor(self):
        sum=0
        
        for i in range(1,self.Value):
            if self.Value %i==0:
                sum=sum+i
        print(f"Sum of the factor is : {sum}")

    def Perfect(self): 
        sum=0
        for i in range(1,self.Value):
            if self.Value %i==0:
                sum=sum+i

        if self.Value==sum:
            print("true")
        else:
            print("False")


    def Display(self):
        self.ChkPrime()
        self.Factor()
        self.SumFactor()
        self.Perfect()


obj1=Numbers()
print("----first obj------")
obj1.Display()




