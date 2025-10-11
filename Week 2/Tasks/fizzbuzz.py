def main():
    try:
        m = int(input("FizzBuzz up to: "))
    except ValueError:
        print("Please enter a whole number.")
        return
    for i in range(1, m+1):
        out = ""
        if i % 3 == 0: out += "Fizz"
        if i % 5 == 0: out += "Buzz"
        print(out or i)

if __name__ == "__main__":
    main()
