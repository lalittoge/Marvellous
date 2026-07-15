class BankAccount:
    ROI=10.5
    def __init__(self):
        self.Name=input("Enter the name")
        self.Amount=int(input("Enter the amount"))


    def Deposit(self):
        self.dp=int(input("Enter the amount shound to be deposite:"))
        self.Amount=self.Amount+self.dp
        print(f"Now total bal become:{self.Amount}")

    def Withdraw(self):
        if self.Amount > 0:
            self.wd=int(input("Enter the amount shound to be withdraw:"))
            self.Amount=self.Amount-self.wd
            print(f"Now total bal become:{self.Amount}")

    def CalInterest(self):
        self.interest=(self.Amount*self.ROI)/100
        print(self.interest)


    def Display(self):
        print(self.Name)
        print(self.Amount)
        self.Deposit()
        self.Withdraw()
        self.CalInterest()




obj=BankAccount()
obj.Display()
