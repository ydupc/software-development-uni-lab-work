user_height_cm = int(input("Enter your height (cm): "))
neighbor1_height_cm = int(input("Enter Neighbor 1's height (cm): "))
neighbor2_height_cm = int(input("Enter Neighbor 2's height (cm): "))

sum_height_cm = user_height_cm+neighbor1_height_cm+neighbor2_height_cm
average = sum_height_cm / 3 * 0.393701

print(average, "inches")

