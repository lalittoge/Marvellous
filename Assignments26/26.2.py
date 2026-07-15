class Circle:
    PI=3.14

    def __init__(self):
        self.Radius=0
        self.Area=0
        self.Circumfernce=0

    
    def Accept(self):
        self.Radius=int(input("Enter the radius of the circel:"))

    def CalArea(self):
        self.Area= self.Radius * self.Radius * self.PI
        print("Area is :",self.Area)

    def CalCir(self):
        self.Circumfernce=  2 * self.PI * self.Radius
        print("Circumfernce  is :",self.Circumfernce)
    
    def Display(self):
        self.Accept()
        self.CalArea()
        self.CalCir()


obj =Circle()
obj1 =Circle()


print("----- First Object -----")
obj.Display()

print("\n----- second Object -----")
obj1.Display()


    

