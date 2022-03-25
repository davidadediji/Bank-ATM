data = [0,1,2,3,4,5]

data.reverse()
print(data)

data = ["a", "b", "c", "d", "e", "f", "g", "h"]
new_data=[]

for item in reversed(data):
	new_data.append(item)
print(new_data)



data = [2,3,4,5,6,7]

data[:] = data[::-1]
print(data)