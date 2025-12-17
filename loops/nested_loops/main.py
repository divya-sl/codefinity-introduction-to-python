produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce, dairy]

for i in range(len(groceries)):
    for j in range(len(groceries[i])):
        print(groceries[i][j])