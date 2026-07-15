class Arithmetic:
    def __init__(self):
        self.Value1=0
        self.Value2=0
    

    def Accept(self):
        self.Value1=int(input("Enter the first no:"))
    
        self.Value2=int(input("Enter the second no:"))
        

    def Add(self):
        return self.Value1 + self.Value2
    
    def Sub(self):
        return self.Value1-self.Value2
    
    def Mul(self):
        return self.Value1*self.Value2
    
    def Div(self):
        return self.Value1/self.Value2
    
    

    
    

obj=Arithmetic()

print("Enter values for Object 1")
obj.Accept()

print("\nobject 1")
print("Addition:",obj.Add())
print("Sub is :",obj.Sub())
print("mul:",obj.Mul())
print("div is :",obj.Div())


