prices = [29.99, 45.50, 12.75, 38.20]

for index in range(len(prices)):
    if(index == 0):
        updated_price = prices[index] - prices[index] * 10/100
    elif(index == 1):
        updated_price = prices[index] - prices[index] * 20/100
    elif(index == 2):
        updated_price = prices[index] - prices[index] * 15/100
    elif(index == 3):
        updated_price = prices[index] - prices[index] * 5/100

    prices[index] = updated_price
    print(f"Updated price for item {index}: ${updated_price:.2f}")
