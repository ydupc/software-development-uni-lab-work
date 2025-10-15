from datetime import datetime
def get_valid_date():
    while True:
        y = input("Year: ").strip()
        m = input("Month (1-12): ").strip()
        d = input("Day: ").strip()
        try:
            dt = datetime(int(y), int(m), int(d))
            return dt
        except ValueError:
            print("Sorry, please enter a valid date.")
def ordinal(n):
    return f"{n}{'th' if 11<=n%100<=13 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"
dt = get_valid_date()
print(f"You were born on {dt.strftime('%A')} the {ordinal(dt.day)} of {dt.strftime('%B %Y')}")
