def main():
    no = int(input("Enter the no :"))
    fact = 1
    for i in range(no,1,-1):
        fact = fact * i

    print("Factorial of the no is :",fact)



if __name__ == "__main__":
    main()