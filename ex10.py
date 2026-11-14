wage = {"Ali": 10, "Sara": 12}
work = [("Ali", 45), ("Sara", 38), ("Omid", 40)]
OVERTIME_THRESHOLD = 40
OVERTIME_RATE = 1.5
total_grand = 0


def salary(rate, hours):
    if hours > OVERTIME_THRESHOLD:
        extra_time = hours - OVERTIME_THRESHOLD
        extra_wage = extra_time * OVERTIME_RATE*rate

        result = extra_wage + OVERTIME_THRESHOLD*rate
    else:
        result = rate*hours
    return result


for name, hours in work:
    if name in wage:
        total = salary(wage[name], hours)
        print(name,  total)
        total_grand += total
    else:
        print(f"{name} :not in wage list")

print(f"Total = {total_grand}")
