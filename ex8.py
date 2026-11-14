grades = {"Ali": 18, "Sara": 14, "Reza": 12}
count = 0
# for name in grades:
#     print(f"{name}: {grades[name]}")
#     if grades[name] > 15:
#         count += 1
# print("above 15:", count)

for name, grade in grades.items():
    print(f"{name}: {grade}")
