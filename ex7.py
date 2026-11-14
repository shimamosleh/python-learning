import csv

with open("catalog.csv") as f:
    reader = csv.DictReader(f)

    catalog = {}

    for row in reader:
        catalog[row["name"]] = int(row["price"])
# print(catalog)
order = [("Detector", 20), ("Siren", 5), ("cable", 100)]
DISCOUNT_THRESHOLD = 10
DISCOUNT_RATE = 0.1
Final = 0


def total_price(qty, price):
    if qty > DISCOUNT_THRESHOLD:
        multiplier = 1-DISCOUNT_RATE
        result = multiplier * qty*price
    else:
        result = qty*price
    return (result)


for name, qty in order:
    if name in catalog:
        total = total_price(qty, catalog[name])
        print(name, total)
        Final += total
    else:
        print(name, ":not in catalog")

print("Final= ", Final)
