import decimal
from src.application import transaction

class TransactionInterface:
	def __init__(self):
		self.active = True

		self.commands = {}
		self.commands["help"] = self.help
		self.commands["exit"] = self.exit
		self.commands["list"] = self.list
		self.commands["transfer"] = self.transfer

	def exit(self):
		self.active = False
	def help(self):
		print("help: Display this")
		print("exit: Exit")
		print("list: List all transactions")
		print("transfer: Transfer $$$ between accounts")
	def list(self):
		transactions = transaction.Transaction.list()
		for t in transactions:
			print(t)
	def transfer(self):
		print("Transfer $$$ between accounts...")
		from_number = input("Number of account to transfer from: ")
		to_number = input("Number of account to transfer to: ")
		amount = input("Amount to transfer: ")
		try:
			amount = decimal.Decimal(amount)
		except:
			raise ValueError("Couldn't parse amount as a decimal")
		notes = input("Additional notes (can be blank): ")
		if notes == "":
			notes = None
		transaction.Transaction.transfer(from_number, to_number, amount, notes)
		print("Transferred " + str(amount) + "$ from " + from_number + " to " + to_number)

	def start(self):
		self.active = True
		print("Transaction manager")
		print("Enter \"help\" to get started ;)")
		while self.active:
			try:
				cmd = input("transaction: ")
				if cmd in self.commands:
					self.commands[cmd]()
				else:
					print("Unknown command")
			except EOFError:
				self.active = False
			except Exception as error:
				print("Error:", error)
		print()