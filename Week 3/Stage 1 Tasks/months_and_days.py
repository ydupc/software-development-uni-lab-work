import calendar
from datetime import datetime
def get_year():
    while True:
        try:
            y = int(input("Enter a year: "))
            if 1 <= y <= 9999:
                return y
            print("Sorry, please enter a valid year between 1 and 9999.")
        except ValueError:
            print("Sorry, please enter a valid year.")
year = get_year()
for month in range(1, 13):
    month_name = datetime(year, month, 1).strftime("%B")
    days_in_month = calendar.monthrange(year, month)[1]
    print(month_name)
    parts = []
    for day in range(1, days_in_month+1):
        short = datetime(year, month, day).strftime("%a")
        parts.append(f"{short} {day}")
    print(", ".join(parts))
    print()
