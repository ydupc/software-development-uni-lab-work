def main():
    name = input("Enter your name: ").strip()
    age_text = input("Enter your age (years): ").strip()
    try:
        age = int(age_text)
    except ValueError:
        print("Age must be a whole number.")
        return
    print(f"Hello, {name}! You are {age} years old.")

if __name__ == "__main__":
    main()
