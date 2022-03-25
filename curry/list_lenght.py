# print(len(["hi", "hello", "wassap"]))


greetings = ['hi', 'hurray', "hello"]

for i in range(len(greetings)):
	print(i, greetings[i])

for i, item in enumerate(greetings):
	print(f"the index of {item} is {i} ")
