class BankAtm():

	bank_name = "GTBank"


	def __init__(self, owner, balance):
		
		self.owner = owner
		self.balance = balance

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
h = BankAtm('Hakeem', 250)
print(p)
print(p.bank_name)
print(p.owner)
print(p.deposit(50))
print(p.balance)
print(p.withdraw(155))

print(h.bank_name)
print(h.owner)
print(h.deposit(50))
print(h.balance)
print(h.withdraw(155))