import random, csv
from src import addressdao, clientdao

class Client:
	def __init__(self, clientdao, addressdao):
		self.first_name = clientdao.first_name
		self.last_name = clientdao.last_name
		self.email = clientdao.email
		self.client_number = clientdao.client_number
		self.city = addressdao.city
		self.street = addressdao.street
		self.house_number = addressdao.house_number
		self.additional = addressdao.additional

	def __str__(self):
		return self.client_number + ": " + self.first_name + " " + self.last_name + " (" + self.email + "; " + self.street + " " + self.house_number + ", " + self.city + (": " + self.additional if self.additional != None else "") + ")"

	@classmethod
	def register(cls, first_name, last_name, email, city, street, house_number, additional=None):
		"""
		Registers a new client.
		Parameters:
		`first_name`: First name of the client
		`last_name`: Last name of the client
		`email`: Email address of the client
		`city`: Name of the city the client lives in
		`street`: Name of the street the client lives on
		`house_number`: Number of the building the client lives in
		`additional`: Additional address info, e.g. '3rd floor', can be None
		Returns: The newly created client as an instance of this class.
		"""
		if not isinstance(first_name, str):
			raise TypeError("First name must be a string")
		if not isinstance(last_name, str):
			raise TypeError("Last name must be a string")
		if not isinstance(email, str):
			raise TypeError("Email must be a string")
		if not isinstance(city, str):
			raise TypeError("City must be a string")
		if not isinstance(house_number, str):
			raise TypeError("House number must be a string")
		if not isinstance(additional, str) and additional != None:
			raise TypeError("Additional address info must be a string or empty")
		if len(first_name) <= 0:
			raise ValueError("First name cannot be empty")
		if len(last_name) <= 0:
			raise ValueError("Last name cannot be empty")
		if len(email) <= 0:
			raise ValueError("Email cannot be empty")
		if len(city) <= 0:
			raise ValueError("City cannot be empty")
		if len(street) <= 0:
			raise ValueError("Street cannot be empty")
		if len(house_number) <= 0:
			raise ValueError("House number cannot be empty")
		address = addressdao.AddressDAO(0, city, street, house_number, additional)
		address = addressdao.AddressDAO.create(address)
		client = clientdao.ClientDAO(0, address.id, first_name, last_name, email, str(random.randint(100000000000, 999999999999)))
		client = clientdao.ClientDAO.create(client)
		return cls(client, address)
	@classmethod
	def list(cls):
		"""
		Lists all clients.
		Returns: A list of all clients as instances of this class.
		"""
		clients = clientdao.ClientDAO.readAll()
		res = []
		for c in clients:
			res.append(cls(c, addressdao.AddressDAO.read(c.address_id)))
		return res
	@classmethod
	def importCSV(cls, filepath):
		"""
		Imports clients from a CSV file.
		The CSV must be in the following format:
		first_name,last_name,email,city,street,house_number,additional_address_info_(can_be_blank)
		Parameters:
		`filepath`: Path to the CSV file to import from.
		"""
		counter = 0
		with open(filepath, newline="") as file:
			reader = csv.reader(file, delimiter=",", quotechar="\"")
			for row in reader:
				if len(row) != 7:
					raise ValueError("Malformed CSV; must be like first_name,last_name,email,city,street,house_number,additional")
				if row[6] == "":
					row[6] = None
				cls.register(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
				counter += 1
		return counter