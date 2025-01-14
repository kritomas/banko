import decimal
from src import account

class AccountInterface:
	def __init__(self):
		self.active = True

		self.commands = {}
		self.commands["help"] = self.help
		self.commands["exit"] = self.exit
		self.commands["open"] = self.open
		self.commands["close"] = self.close
		self.commands["list"] = self.list
		self.commands["deposit"] = self.deposit
		self.commands["withdraw"] = self.withdraw

	def exit(self):
		self.active = False
	def help(self):
		print("help: Display this")
		print("exit: Exit")
		print("open: Open new account")
		print("close: Close account")
		print("list: List all accounts")
		print("deposit: Deposit into account")
		print("withdraw: Withdraw from account")
	def open(self):
		print("Opening new account...")
		client_number = input("Number of owner: ")
		bank_number = input("Number of bank: ")
		account_type = input("Type of account (\"basic\"/\"savings\"): ")
		a = account.Account.open(client_number, bank_number, account_type)
		print("Opened new account with number", a.account_number)
	def close(self):
		print("Closing account...")
		account_number = input("Number of account: ")
		confirmation = input("Really close? (y/N): ")
		if (confirmation == "y" or confirmation == "Y"):
			a = account.Account.close(account_number)
			print("Closed account with number", a.account_number)
		else:
			print("Aborting.")
	def list(self):
		accounts = account.Account.list()
		for a in accounts:
			print(a)
	def deposit(self):
		print("Depositing $$$ into account...")
		account_number = input("Number of account: ")
		amount = input("Amount to deposit: ")
		try:
			amount = decimal.Decimal(amount)
		except:
			raise ValueError("Couldn't parse amount as a decimal")
		account.Account.deposit(account_number, amount)
		print("Deposited " + str(amount) + "$ into " + account_number)
	def withdraw(self):
		print("Withdrawing $$$ from account...")
		account_number = input("Number of account: ")
		amount = input("Amount to withdraw: ")
		try:
			amount = decimal.Decimal(amount)
		except:
			raise ValueError("Couldn't parse amount as a decimal")
		account.Account.withdraw(account_number, amount)
		print("Withdrawn " + str(amount) + "$ from " + account_number)

	def start(self):
		self.active = True
		print("Account manager")
		print("Enter \"help\" to get started ;)")
		while self.active:
			try:
				cmd = input("account: ")
				if cmd in self.commands:
					self.commands[cmd]()
				else:
					print("Unknown command")
			except EOFError:
				self.active = False
			except Exception as error:
				print("Error:", error)
		print()