def main():
    try:
        n = int(input("Sum from 1 to n, n = "))
    except ValueError:
        print("Please enter a whole number.")
        return
    if n < 1:
        print("n must be at least 1.")
        return
    # Using formula and a loop to show both approaches
    formula = n * (n + 1) // 2
    print(f"Sum (formula) = {formula}")
    total = 0
    for i in range(1, n+1):
        total += i
    print(f"Sum (loop)    = {total}")

if __name__ == "__main__":
    main()
