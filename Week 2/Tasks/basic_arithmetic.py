def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return
    print(f"{a} + {b} = {a+b}")
    print(f"{a} - {b} = {a-b}")
    print(f"{a} * {b} = {a*b}")
    if b != 0:
        print(f"{a} / {b} = {a/b}")
        print(f"{a} // {b} = {a//b}")
        print(f"{a} % {b} = {a%b}")
    else:
        print("Division by zero is undefined.")

if __name__ == "__main__":
    main()
