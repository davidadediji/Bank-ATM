class BankAtm():


	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance
	
	def __str__(self):
		return f"Owner: {self.owner}\nCurrent Balance: {self.balance}"

	def deposit(self, amount_deposited):
		
		self.balance += amount_deposited
		return "Deposit accepted"
		

	def withdraw(self, withdraw_amount):
	
		if withdraw_amount < self.balance:
			self.balance -= withdraw_amount
			return "withdrawal accepted"
		else:
			return "funds unavaliable"

p = BankAtm('david', 100)
print(p)
print(p.deposit(50))
print(p.balance)
print(p.withdraw(155))