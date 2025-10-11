import math

def main():
    try:
        r = float(input("Radius: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    if r < 0:
        print("Radius cannot be negative.")
        return
    area = math.pi * r ** 2
    print(f"Area = {area:.4f}")

if __name__ == "__main__":
    main()
