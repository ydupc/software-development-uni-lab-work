def main():
    try:
        mass = float(input("Mass (kg): "))
        height = float(input("Height (m): "))
    except ValueError:
        print("Please enter valid numbers.")
        return
    if height <= 0:
        print("Height must be positive.")
        return
    bmi = mass / (height ** 2)
    if   bmi < 18.5: cat = "Underweight"
    elif bmi < 25:   cat = "Normal"
    elif bmi < 30:   cat = "Overweight"
    else:            cat = "Obese"
    print(f"BMI = {bmi:.2f} ({cat})")

if __name__ == "__main__":
    main()
