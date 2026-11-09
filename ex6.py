catalog = {"Detector": 35, "siren": 60, "Panel": 400}
order = [("Detector", 20), ("siren", 5), ("Cable", 100)]

DISCOUNT_THRESHOLD = 10
DISCOUNT_RATE = 0.1
grand_total = 0


def total_price(qty, price):
    if qty > DISCOUNT_THRESHOLD:
        multiplier = 1-DISCOUNT_RATE
        total = multiplier * qty*price
    else:
        total = qty*price
    return total


for name, qty in order:
    if name in catalog:
        result = total_price(qty, catalog[name])
        print(name, result)
        grand_total += result
    else:
        print(f"{name} :not in catalog")
print(f"Grand_Total= {grand_total}")
