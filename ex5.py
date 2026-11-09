items = [("Detector", 20, 35), ("Siren", 5, 60), ("Panel", 1, 400)]
Discount_threshold = 10
Discount_rate = 0.10
final_price = 0


def total_price(quantity, price):
    if quantity > Discount_threshold:
        multiplier = 1-Discount_rate
        total = multiplier * quantity*price
    else:
        total = quantity*price
    return total


for name, quantity, price in items:
    result = total_price(quantity, price)
    print(name, result)
    final_price += result
print(f"Final_price = {final_price}")
