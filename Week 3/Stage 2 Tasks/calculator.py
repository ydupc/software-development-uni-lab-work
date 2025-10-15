def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
def get_op():
    op = input("Which operation do you want (+, -, *, /)? ").strip()
    while op not in {"+","-","*","/"}:
        print("Please enter one of: + - * /")
        op = input("Which operation do you want (+, -, *, /)? ").strip()
    return op
def ask_yes_no(prompt="Do you want another go (y/n): "):
    while True:
        ans = input(prompt).strip().lower()
        if ans in {"y","n"}: return ans == "y"
        print("Please answer 'y' or 'n'.")
while True:
    op = get_op()
    a = get_float("Enter first number: ")
    b = get_float("Enter second number: ")
    if op == "/" and b == 0:
        print("Cannot divide by zero. Try again.")
        continue
    total = {"+": a+b, "-": a-b, "*": a*b, "/": a/b}[op]
    print(f"{a} {op} {b} = {total}")
    if not ask_yes_no(): break
