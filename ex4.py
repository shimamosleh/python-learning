
DISCOUNT_THRESHOLD = 10
DISCOUNT_RATE = 0.2


def total_price(quantity, unit_price):

    if quantity > DISCOUNT_THRESHOLD:
        discount_rate = 1 - DISCOUNT_RATE
        total = discount_rate * (quantity*unit_price)
    else:
        total = quantity * unit_price
    return total


quantity = int(input("Quantity= "))
unit_price = int(input("Unit_price= "))

result = total_price(quantity, unit_price)
print(f"total_price= {result}")
