backpack = ['pizza slice', "button", "pizza slice", "fishing pole",
"pizza slice", "nunchicks", "sandwich from mcdonalds"]

for item in backpack[:]:
	print(item)
	if item == "pizza slice":
		backpack.remove("pizza slice")
# print(backpack)