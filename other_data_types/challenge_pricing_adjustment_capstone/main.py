grocery_inventory = {
    "Milk" : ("Diary", 3.50, 8),
    "Eggs" : ("Diary", 5.50, 30),
    "Bread" : ("Bakery", 2.99, 15),
    "Apples" : ("Produce", 1.50, 50)
}

egg_details = grocery_inventory.get("Eggs")
if(egg_details[1] > 5):
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = ("Diary", 4.50, 30)
    #print(f"updated egg price: {grocery_inventory.get("Eggs")[1]}")
else:
    print("The price of Eggs is reasonable.")

grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print(f"Inventory after adding Tomatoes: {grocery_inventory}")

milk_details = grocery_inventory.get("Milk")
if(milk_details[2] < 10):
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = ("Diary", 3.50, 28)
    #print(f"updated milk details: {grocery_inventory.get("Milk")[2]}")
else:
    print("Milk had sufficient stock.")

if(grocery_inventory.get("Apples")[1] > 2):
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print(f"Updated inventory: {grocery_inventory}")