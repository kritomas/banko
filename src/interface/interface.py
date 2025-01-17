from src.interface import clientinterface, bankinterface, accountinterface, transactioninterface

class Interface:
	def __init__(self):
		self.active = True

		self.commands = {}
		self.commands["help"] = self.help
		self.commands["exit"] = self.exit
		self.commands["client"] = clientinterface.ClientInterface().start
		self.commands["bank"] = bankinterface.BankInterface().start
		self.commands["account"] = accountinterface.AccountInterface().start
		self.commands["transaction"] = transactioninterface.TransactionInterface().start

	def exit(self):
		self.active = False
	def help(self):
		print("help: Display this")
		print("exit: Exit")
		print("client: Manage clients")
		print("bank: Manage banks")
		print("account: Manage accounts")
		print("transaction: Manage transactions")

	def start(self):
		self.active = True
		print("Welcome to Banqo, your no. 1 bank management system!")
		print("Enter \"help\" to get started ;)")
		while self.active:
			try:
				cmd = input(": ")
				if cmd in self.commands:
					self.commands[cmd]()
				else:
					print("Unknown command")
			except EOFError:
				self.active = False
			except Exception as error:
				print("Error:", error)
		print("Cya")