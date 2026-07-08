def Divide(no):
    if no % 5 ==0:
        return True
    else:
        return False

def main():
    no = int(input("Enter the no "))
    Ret = Divide(no)
    if (Ret== True):
        print("True")
    else:
        print("False")
if __name__ == "__main__":
    main()