def main():
    try:
        n = int(input("n (0–20 recommended): "))
    except ValueError:
        print("Please enter a whole number.")
        return
    if n < 0:
        print("n must be non-negative.")
        return
    fact = 1
    for i in range(2, n+1):
        fact *= i
    print(f"{n}! = {fact}")

if __name__ == "__main__":
    main()
