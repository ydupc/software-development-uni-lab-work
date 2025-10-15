VALID_MIN, VALID_MAX = 1900, 2011
REFERENCE_YEAR = 2011
while True:
    try:
        year = int(input("What year were you born? "))
        if VALID_MIN <= year <= VALID_MAX:
            break
        print("Sorry, please enter a valid year.")
    except ValueError:
        print("Sorry, please enter a valid year.")
age = REFERENCE_YEAR - year
print(f"You are about {age} years old.")
