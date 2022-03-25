class BankAtm():
  
	bank_name = "GTBank"
 

	def __init__(self, owner, balance):
		self.owner_x = owner
		self.balance_y = balance
		self.bank_name = 'FirstBank'

	def deposit(self, amount_deposited):
		self.balance_y += amount_deposited
		return "Deposit accepted"


	def withdraw(self, withdraw_amount):
	
		if withdraw_amount < self.balance_y:
			self.balance_y -= withdraw_amount
			return "withdrawal accepted"
		else:
			return "funds unavaliable"

p = BankAtm('david', 100)
h = BankAtm('Hakeem', 250)
print(p)
print(p.bank_name)
print(p.owner_x)
print(p.deposit(50))
print(p.balance_y)
print(p.withdraw(155))

print(h.bank_name)
print(h.owner_x)
print(h.deposit(50))
print(h.balance_y)
print(h.withdraw(155))