class Cat:
	species = 'mammal'

	def __init__(self, name="anonymous", age = 0):
		self.name = name
		self.age = age


cat1 = Cat('uranus', 120)
cat2 = Cat('Trem', 15)
cat3 = Cat('Tems', 45)

def oldest(*args):
	max = 0
	for num in args:
		if num > max:
			max = num
	return max 
print(f"The cat with the oldest age is {oldest(cat1.age, cat2.age, cat3.age)}")

