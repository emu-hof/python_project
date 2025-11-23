# 2. Simple Grocery Cart Checkout
# Write a program that:
# Has a predefined dictionary of groceries with prices.
# Lets the user “add” items by typing their names.
# For each valid item, asks for the quantity.
# Keeps adding to the cart until the user types "checkout".
# Displays a final bill: each item, quantity, subtotal, and total.
# Skills practiced: dictionaries, loops, input(), math operations, formatting, error handling

items={
    "BANANA": 130,
    "EGG" : 22,
    "YOGURT": 110,
    "CHEESE": 252
}
cart={}
print("Welcome to Fresh Grocery")
print("-----Fresh's Menu------")
for i in items:
    print(i,"->",items[i])
while True:
 Choice=input("Enter item name to add items or type 'checkout' to exit: ").strip().upper()
 if Choice in items:
    try:
        quantity=int(input("Please enter quantity: ").strip())
        if quantity <= 0:
                print("Quantity must be a positive number.")
                continue
        cart[Choice] = cart.get(Choice, 0) + quantity

    except ValueError:
       print("Please enter a valid whole number")
 elif Choice == "CHECKOUT":
   break
 else:
   print("item is not available")
# Displays a final bill: each item, quantity, subtotal, and total.
print("---Bill Summary---")
Total=0
for addItem, quantity in cart.items():
   price = items[addItem]
   subTotal=quantity*price
   Total= subTotal+Total
   print(addItem,"X",quantity," = ",subTotal)
print("Total Price=", Total)