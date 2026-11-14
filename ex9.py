words = ["siren", "panel", "siren", "detector", "panel", "siren"]
counts = {}

for word in words:
    counts[word] = counts.get(word, 0)+1
#     if word in counts:
#         counts[word] += 1

#     else:
#         counts[word] = 1
print(counts)
