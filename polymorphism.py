class Dog():

	def __init__(self, name):
		self.name = name 

	def speak(self):
		return self.name + " says whoof!"

class Cat():
	
	def __init__(self, name):
		self.name = name 

	def speak(self):
		return self.name + " says meow!"



niko = Dog("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())


for pet_class in [niko, felix]:
	print(type(pet_class))
	print(pet_class.speak())

def pet_speak(pet_class):
	print(pet_class.speak())

pet_speak(felix )