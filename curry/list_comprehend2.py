backpack = ["sword", "rubber duck", "sword", "slice of pizza"]

counts = backpack.count('sword')

print(counts)


counts = [[backpack.count(item), item] for item in set(backpack)]
print(counts)

[print(backpack.count(item), item) for item in set(backpack)]