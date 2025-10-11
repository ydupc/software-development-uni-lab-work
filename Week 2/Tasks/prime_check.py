def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    try:
        n = int(input("Check if prime, n = "))
    except ValueError:
        print("Please enter a whole number.")
        return
    print(f"{n} is {'prime' if is_prime(n) else 'not prime'}.")

if __name__ == "__main__":
    main()
