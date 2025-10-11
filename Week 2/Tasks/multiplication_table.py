def main():
    try:
        n = int(input("Show times table for: "))
    except ValueError:
        print("Please enter a whole number.")
        return
    for i in range(1, 13):
        print(f"{n} x {i:2} = {n*i}")

if __name__ == "__main__":
    main()
