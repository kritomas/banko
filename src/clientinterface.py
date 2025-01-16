from src import client

class ClientInterface:
	def __init__(self):
		self.active = True

		self.commands = {}
		self.commands["help"] = self.help
		self.commands["exit"] = self.exit
		self.commands["register"] = self.register
		self.commands["list"] = self.list
		self.commands["report"] = self.report
		self.commands["import"] = self.importCSV

	def exit(self):
		self.active = False
	def help(self):
		print("help: Display this")
		print("exit: Exit")
		print("register: Register new client")
		print("list: List all clients")
		print("report: List all clients with their total balances accross all accounts")
		print("import: Import clients from a CSV file")
	def register(self):
		print("Registering new client...")
		first_name = input("First name: ")
		last_name = input("Last name: ")
		email = input("Email: ")
		city = input("City: ")
		street = input("Street: ")
		house_number = input("House number: ")
		additional = input("Additional address info (can be blank): ")
		if additional == "":
			additional = None
		c = client.Client.register(first_name, last_name, email, city, street, house_number, additional)
		print("Registered new client with number", c.client_number)
	def list(self):
		clients = client.Client.list()
		for c in clients:
			print(c)
	def report(self):
		report = client.Client.report()
		for r in report:
			print(r)
	def importCSV(self):
		print("Importing clients from CSV...")
		filepath = input("Filepath: ")
		c = client.Client.importCSV(filepath)
		print("Imported", c, "clients")

	def start(self):
		self.active = True
		print("Client manager")
		print("Enter \"help\" to get started ;)")
		while self.active:
			try:
				cmd = input("client: ")
				if cmd in self.commands:
					self.commands[cmd]()
				else:
					print("Unknown command")
			except EOFError:
				self.active = False
			except Exception as error:
				print("Error:", error)
		print()