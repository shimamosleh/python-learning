prices = [120, 450, 80, 300]
total = 0
for price in prices:
    total += price
print(f"total= {total}")
for price in prices:
    if price > 100:
        print(price)
