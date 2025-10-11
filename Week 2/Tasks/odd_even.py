def main():
    try:
        n = int(input("Enter an integer: "))
    except ValueError:
        print("Please enter a whole number.")
        return
    print("Even" if n % 2 == 0 else "Odd")

if __name__ == "__main__":
    main()
