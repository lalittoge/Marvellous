def Marks(mark):
    if(mark>=75):
        print("Destination")
    elif(mark>=60):
        print("First class")
    elif(mark>=50):
        print("Second class")
    else:
        print("Fail")


def main():
    no = (int(input("Enter the marks")))
    Marks(no)

if __name__ == "__main__":
    main()