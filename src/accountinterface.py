from src import account

class AccountInterface:
	def __init__(self):
		self.active = True

		self.commands = {}
		self.commands["help"] = self.help
		self.commands["exit"] = self.exit
		self.commands["open"] = self.open
		self.commands["list"] = self.list

	def exit(self):
		self.active = False
	def help(self):
		print("help: Display this")
		print("exit: Exit")
		print("open: Open new account")
		print("list: List all accounts")
	def open(self):
		print("Opening new account...")
		client_number = input("Number of owner: ")
		bank_number = input("Number of bank: ")
		account_type = input("Type of account (\"basic\"/\"savings\"): ")
		a = account.Account.open(client_number, bank_number, account_type)
		print("Registered new account with number", a.account_number)
	def list(self):
		accounts = account.Account.list()
		for a in accounts:
			print(a)

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