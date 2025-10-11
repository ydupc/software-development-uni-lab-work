user_height_ft = int(input("Enter your height (feet): "))
user_heigh_in = int(input("Enter your height (inches): "))
neighbor1_height_ft = int(input("Enter Neighbor 1's height (ft): "))
neighbor1_height_in = int(input("Enter Neighbor 1's height (inches): "))
neighbor2_height_ft = int(input("Enter Neighbor 2's height (ft): "))
neighbor2_height_in = int(input("Enter Neighbor 2's height (inches): "))

average = (neighbor1_height_ft + neighbor2_height_ft) / 2

print(f"{average} Ft.")
