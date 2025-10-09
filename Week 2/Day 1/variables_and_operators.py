# See the week 2 tasks pdf for more information.itemPrice = float(input("Enter the item price: ")) itemTax

itemPrice = float(input("Enter the item price: "))
itemTax = itemPrice * 20 / 100   # or itemPrice * 0.2
totalPrice = itemPrice + itemTax

print("The total price (including 20% tax) is:", totalPrice)

numItems = int(input("How many items do you want to buy? "))
totalCost = totalPrice * numItems

print("The price for", numItems, "items is", format(totalCost, ".2f"))