menu={"1":("chips", 4.78),
      "2":("popcorn", 3.22),
      "3":("poptart", 9.45),
      "4":("fruit_cup",7.80),
      "5":("cheese_plate", 12.25),
      "6":("coke", 3.00),
      "7":("water",1.54),
      "8":("hot chocolate", 2.57),
      "9":("sprite",2.63),
      "10":("juice",5.52)
}
print("Hello, welcome to  M&M vending. The items avaliable are")
for item_number, (snack,price) in menu.items():
    print(f"{item_number}. {snack} ${price:.2f}")
item_picked=[]
total_due=0.00
while True:
    item_choice=input("choose the an item. Please type stop once completed").strip(). lower()
    if item_choice == "done":
        break
    if item_choice in menu:
        item_menu,item_price=menu[item_choice]
        item_picked.append((item_menu, item_price))
        total_due +=item_price
    else:
        print("ERROR!! MAKE A VALID SELECTION")
print("M&M vending receipt")
for snack, price in item_picked:
    print(f"{snack} $ {price:.2f}")
print(f"Total Due $ {total_due:.2f}") 
