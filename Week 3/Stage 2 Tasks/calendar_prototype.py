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
    days = calendar.monthrange(year, month)[1]
    month_name = datetime(year, month, 1).strftime("%B")
    first_weekday = datetime(year, month, 1).strftime("%A")
    print(f"{month_name}\n{days} days (starts on {first_weekday})")
