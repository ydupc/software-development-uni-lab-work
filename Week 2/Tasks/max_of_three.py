def main():
    try:
        x = float(input("x: "))
        y = float(input("y: "))
        z = float(input("z: "))
    except ValueError:
        print("Please enter valid numbers.")
        return
    print(f"Max is {max(x, y, z)}")

if __name__ == "__main__":
    main()
