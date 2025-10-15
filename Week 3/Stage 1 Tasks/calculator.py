def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
def get_op():
    op = input("Which operation do you want + or - ? ").strip()
    while op not in {"+","-"}:
        print("Please enter '+' or '-'")
        op = input("Which operation do you want + or - ? ").strip()
    return op
while True:
    op = get_op()
    a = get_float("Enter first number: ")
    b = get_float("Enter second number: ")
    total = a + b if op == "+" else a - b
    print(f"{a} {op} {b} = {total}")
    yesNo = input("Do you want another go (y/n): ").strip().lower()
    while yesNo not in {"y","n"}:
        print("Please answer 'y' or 'n'.")
        yesNo = input("Do you want another go (y/n): ").strip().lower()
    if yesNo == "n":
        break
