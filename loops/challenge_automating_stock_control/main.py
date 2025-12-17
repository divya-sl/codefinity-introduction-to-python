# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")

for item, values in inventory.items():
    print(f"Processing {item}")
    #print(f"{item} has a current stock of {values[0]}, minimum required stock of {values[1]}, restock quantity of {values[2]}, and sale status of {values[3]}")
    while(values[0] < values[1]):
        values[0] += values[2]
        #print(f"Increasing stock of {item} by {values[2]}, current stock now is {values[0]}")

    if(values[0] > discount_threshold and values[3] == False):
        values[3] = True

#for item, values in inventory.items():
    #print(f"Processing {item}")
    #print(f"{item} has a current stock of {values[0]}, minimum required stock of {values[1]}, restock quantity of {values[2]}, and sale status of {values[3]}")

print("Processing completed")