import calendar
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
    print(f"Month {month}\n{days} days")
