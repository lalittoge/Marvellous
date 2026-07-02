def Circle(no):
    return 3.14 * no

def main():
    radius = int(input("Enter the radius of circle:"))
    area = Circle(radius)

    print("Area of the circle:",area )



if __name__ == "__main__":
    main()