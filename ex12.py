catalog = {"Detector": 35, "Siren": 60, "Panel": 400}
order = [("Detector", 20), ("Siren", 5), ("Cable", 100)]
DISCOUNT_THRESHOLD = 10
DISCOUNT_RATE = 0.1


def total_price(qty, price):

    if qty > DISCOUNT_THRESHOLD:
        multiplier = 1-DISCOUNT_RATE
        result = multiplier * qty*price
    else:
        result = qty * price
    return result


def process_order(catalog, order):
    total = 0
    missing = []
    for device, qty in order:
        if device in catalog:
            row_price = total_price(qty, catalog[device])
            total += row_price

        else:
            missing.append(device)

    return total, missing


total, missing = process_order(catalog, order)

print(f"Total= {total}")
print(f"Missing:{missing}")
