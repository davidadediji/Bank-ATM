print("what your favourite veggies.\nhit enter after each food")

# data = input()

# favs = data.split()

# for food in favs:
# 	print(food)

favs = []
while True:
	data = input()
	if str.lower(data) == 'q':
		break
	favs.append(data)

for food in favs:
	print("you said", food)