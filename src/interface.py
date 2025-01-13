class Interface:
	def __init__(self):
		self.active = True

		self.commands = {}
		self.commands["help"] = self.help
		self.commands["exit"] = self.exit

	def exit(self):
		self.active = False
	def help(self):
		print("help: Display this")
		print("exit: Exit")

	def start(self):
		print("Welcome to Banko, your no. 1 bank management system!")
		print("Enter \"help\" to get started ;)")
		while self.active:
			try:
				cmd = input(": ")
				if cmd in self.commands:
					self.commands[cmd]()
				else:
					print("Unknown command")
			#except KeyboardInterrupt:
			#	print("Type \"exit\" to exit")
			except EOFError:
				self.active = False
			except Exception as error:
				print("Error:", error)
		print("Cya")