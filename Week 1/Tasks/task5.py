user_height_cm = int(input("Enter your height (cm): "))
neighbor1_height_cm = int(input("Enter Neighbor 1's height (cm): "))
neighbor2_height_cm = int(input("Enter Neighbor 2's height (cm): "))

sum_height_cm = user_height_cm+neighbor1_height_cm+neighbor2_height_cm
average = (user_height_cm+neighbor1_height_cm+neighbor2_height_cm)/3
inches = average * 0.3937
feet = average * 0.0328

print(f"{feet} ft, {inches} in.")

