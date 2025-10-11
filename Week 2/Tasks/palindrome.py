def main():
    s = input("Enter text: ").strip()
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    print("Palindrome" if cleaned == cleaned[::-1] else "Not a palindrome")

if __name__ == "__main__":
    main()
