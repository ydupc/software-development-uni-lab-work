def main():
    try:
        c = float(input("Temperature in °C: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    f = (c * 9/5) + 32
    print(f"{c}°C = {f:.2f}°F")

if __name__ == "__main__":
    main()
