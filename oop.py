class NameOfPerson:

	def __init__(self, firstname, lastname, location, age, gender):
		self.firstname = firstname
		self.lastname = lastname
		self.location = location
		self.age = age
		self.gender = gender
	
	def description(self):
		return f"{self.firstname} {self.lastname} stays in {self.location}, he is a {self.age} year old {self.gender}"

p = NameOfPerson('David', 'Adediji', 'Lagos, Nigeria', 23, 'Male')
print(p.description())
