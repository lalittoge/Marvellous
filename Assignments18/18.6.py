

def main():
    no = int(input("Enter the no:"))
    for i in range(no,0,-1):
        for j in range(i):
            print("*", end=" ")
        print()

if __name__ == "__main__":
    main()