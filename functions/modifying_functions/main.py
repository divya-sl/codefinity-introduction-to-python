def apply_discount(price, discount=0.05):
    return float(price * (1.00 - float(discount)))

def apply_tax(price, tax=0.07):
    return float(price * (1.00 + float(tax)))

def calculate_total(price, discount=0.05, tax=0.07):
    #print("tax", apply_tax(price, tax))
    #print("discount", apply_discount(price, discount))
    #print("price :", price * (1+ tax) * (1-discount))
    
    return price * (1+ tax) * (1-discount)

total_price_default = calculate_total(120)
print(f"Total cost with default discount and tax: ${total_price_default:.2f}")
total_price_custom = calculate_total(100, discount=0.10, tax=0.08)
print(f"Total cost with custom discount and tax: ${total_price_custom:.2f}")