data = ["a", "c", "b", "d", "e", "f", "g", "h"]

for index in range(len(data)//2):
	data[index], data[-index-1] = data[-index-1], data[index]
print(data)




# print(data[index], data[-index-1])
# data[index], data[-index-1] = data[-index-1], data[index]
# print(data[index], data[-index-1])





# me = "Caleb"

# you = "Suscriber"

# print(me, you)
# me, you = you, me
# print(me, you)