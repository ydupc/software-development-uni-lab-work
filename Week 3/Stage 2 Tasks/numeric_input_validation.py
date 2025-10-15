def get_valid_year(min_year=1900, max_year=2011):
    while True:
        try:
            y = int(input("What year were you born? "))
            if min_year <= y <= max_year:
                return y
            print(f"Sorry, please enter a valid year between {min_year} and {max_year}.")
        except ValueError:
            print("Sorry, please enter a valid year.")
REFERENCE_YEAR = 2011
year = get_valid_year()
print(f"You are about {REFERENCE_YEAR - year} years old.")
