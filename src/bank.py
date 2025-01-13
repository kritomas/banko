import random
from src import addressdao, bankdao

class Bank:
	def __init__(self, bankdao, addressdao):
		self.bank_number = bankdao.bank_number
		self.city = addressdao.city
		self.street = addressdao.street
		self.house_number = addressdao.house_number
		self.additional = addressdao.additional

	def __str__(self):
		return self.bank_number + ": " + self.street + " " + self.house_number + ", " + self.city + (": " + self.additional if self.additional != None else "")

	@classmethod
	def register(cls, city, street, house_number, additional=None):
		address = addressdao.AddressDAO(0, city, street, house_number, additional)
		address = addressdao.AddressDAO.create(address)
		bank = bankdao.BankDAO(0, address.id, str(random.randint(100000000000, 999999999999)))
		bank = bankdao.BankDAO.create(bank)
		return cls(bank, address)
	@classmethod
	def list(cls):
		banks = bankdao.BankDAO.readAll()
		res = []
		for b in banks:
			res.append(cls(b, addressdao.AddressDAO.read(b.address_id)))
		return res