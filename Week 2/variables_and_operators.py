# See the week 2 tasks pdf for more information.itemPrice = float(input("Enter the item price: ")) itemTax

itemPrice = float(input("Enter the item price: "))
itemTax = 8.5

totalPrice = itemPrice + (itemPrice * itemTax / 100)
print("The total price is: ", totalPrice)