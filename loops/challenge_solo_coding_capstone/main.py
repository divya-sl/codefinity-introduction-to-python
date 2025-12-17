# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

for item, values in inventory.items():
    if values[0] < 30:
        print(f"{item} need restocking.")
    elif values[0] > 100:
        print(f"{item} should be sold at the discounted price of {values[2]}.")
    else:
        print(f"{item} should be sold at the regular price of {values[1]}.")
        