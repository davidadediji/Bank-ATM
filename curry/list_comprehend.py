healthy = ["Kale chips", "broccoli"]
backpack = ["pizza", "frozen custard", "apple crips", "Kale chips"]
print(id(backpack))

backpack[:] = [item for item in backpack if item in healthy] #create a copy of a list
print(id(backpack))
print(backpack)


squares = [i**2 for i in range(10) if i % 2 ==0]
print(squares)

greetings = ["hi", "hello", "wassap"]

cap_greetings = [item.capitalize() for item in greetings if item.startswith('h')]
print(cap_greetings)
