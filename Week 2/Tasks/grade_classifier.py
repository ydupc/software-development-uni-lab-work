def main():
    try:
        mark = float(input("Enter mark (0–100): "))
    except ValueError:
        print("Please enter a valid number.")
        return
    if not 0 <= mark <= 100:
        print("Mark must be between 0 and 100.")
        return
    if mark >= 70:
        grade = "First"
    elif mark >= 60:
        grade = "Upper Second (2:1)"
    elif mark >= 50:
        grade = "Lower Second (2:2)"
    elif mark >= 40:
        grade = "Third"
    else:
        grade = "Fail"
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
