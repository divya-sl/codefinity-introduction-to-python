# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

range_value = 0
if len(daily_promotions) <= len(weekdays):
    range_value = len(daily_promotions)
else:
    range_value = len(weekdays)

for i in range(range_value):
    print(f"{weekdays[i]}: Promotion on {daily_promotions[i]}")
