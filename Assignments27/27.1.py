class BookStore:
    NoOfBooks=0
    def __init__(self,Bookname,Bookauthor):
        self.Name=Bookname
        self.Author=Bookauthor

        if(self.Name):
            BookStore.NoOfBooks=BookStore.NoOfBooks+1

    def Display(self):
        print(f"{self.Name} by {self.Author} no of book {self.NoOfBooks}")


obj=BookStore("Enjoy","Lalit")
obj.Display()

obj1=BookStore("Enjoy1","Lalit1")
obj1.Display()