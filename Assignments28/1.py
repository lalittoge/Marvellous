import sys

def main():
    filename=input("Enter the filename:")
    fobj=open(filename,"r")
    count=0
    for line in fobj:
        count+=1
    print("No of lines in the file:",count)

    fobj.close()

if __name__ == "__main__":
    main()