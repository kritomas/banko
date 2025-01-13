import random
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

	@classmethod
	def register(cls, first_name, last_name, email, city, street, house_number, additional=None):
		address = addressdao.AddressDAO(0, city, street, house_number, additional)
		address = addressdao.AddressDAO.create(address)
		client = clientdao.ClientDAO(0, address.id, first_name, last_name, email, str(random.randint(100000000000, 999999999999)))
		client = clientdao.ClientDAO.create(client)
		return cls(client, address)