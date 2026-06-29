def main():
    char = input("Enter the character :").lower()
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u') :
        print("vowel")
    else:
        print("consoant")

if __name__ == "__main__":
    main()