from src import bank

class BankInterface:
	def __init__(self):
		self.active = True

		self.commands = {}
		self.commands["help"] = self.help
		self.commands["exit"] = self.exit
		self.commands["register"] = self.register
		self.commands["list"] = self.list

	def exit(self):
		self.active = False
	def help(self):
		print("help: Display this")
		print("exit: Exit")
		print("register: Register new bank")
		print("list: List all banks")
	def register(self):
		print("Registering new bank...")
		city = input("City: ")
		street = input("Street: ")
		house_number = input("House number: ")
		additional = input("Additional address info (can be blank): ")
		if additional == "":
			additional = None
		b = bank.Bank.register(city, street, house_number, additional)
		print("Registered new bank with number", b.bank_number)
	def list(self):
		banks = bank.Bank.list()
		for b in banks:
			print(b)

	def start(self):
		self.active = True
		print("Bank manager")
		print("Enter \"help\" to get started ;)")
		while self.active:
			try:
				cmd = input("bank: ")
				if cmd in self.commands:
					self.commands[cmd]()
				else:
					print("Unknown command")
			except EOFError:
				self.active = False
			except Exception as error:
				print("Error:", error)
		print()