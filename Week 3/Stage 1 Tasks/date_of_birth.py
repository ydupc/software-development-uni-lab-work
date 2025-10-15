from datetime import datetime
def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
def get_valid_date():
    while True:
        y = read_int("Year: ")
        m = read_int("Month (1-12): ")
        d = read_int("Day: ")
        try:
            dt = datetime(y, m, d)
            return dt
        except ValueError:
            print("Sorry, please enter a valid date.")
dt = get_valid_date()
print(f"You were born on a {dt.strftime('%A')}")
