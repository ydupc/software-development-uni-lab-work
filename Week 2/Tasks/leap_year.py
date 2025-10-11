def main():
    try:
        y = int(input("Year: "))
    except ValueError:
        print("Please enter a whole number.")
        return
    leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
    print("Leap year" if leap else "Not a leap year")

if __name__ == "__main__":
    main()
