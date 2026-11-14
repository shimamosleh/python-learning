catalog = {"Cable": 2, "Detector": 35.7}
order = [("Cable", 100), ("Detector", 3), ("Relay", 4)]
VAT_RATE = 0.09
subtotal = 0
for device, qty in order:
    if device in catalog:
        price = qty*catalog[device]
        print(f"{device} {price}")
        subtotal += price
    else:
        print(f"{device} :not in catalog")
print(f"Subtotal = {subtotal}")
vat = round(VAT_RATE*subtotal, 2)
print(f"VAT= {vat}")
total = vat + subtotal
print(f"Total = {round(total, 2)}")
