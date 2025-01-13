import random, datetime, decimal
from src import accountdao, clientdao, bankdao

class Account:
	def __init__(self, accountdao, clientdao, bankdao):
		self.client_number = clientdao.client_number
		self.bank_number = bankdao.bank_number
		self.account_number = accountdao.account_number
		self.account_type = accountdao.account_type
		self.is_frozen = accountdao.is_frozen
		self.created_on = accountdao.created_on
		self.balance = accountdao.balance

	def __str__(self):
		return self.account_number + ": Owned by " + self.client_number + " at " + self.bank_number + " (" + str(self.balance) + "$)"

	@classmethod
	def open(cls, client_number, bank_number, account_type):
		client = clientdao.ClientDAO.readByClientNumber(client_number)
		bank = bankdao.BankDAO.readByBankNumber(bank_number)
		account = accountdao.AccountDAO(0, client.id, bank.id, account_type, str(random.randint(100000000000, 999999999999)), False, datetime.datetime.now(), decimal.Decimal(0))
		account = accountdao.AccountDAO.create(account)
		return cls(account, client, bank)
	@classmethod
	def list(cls):
		accounts = accountdao.AccountDAO.readAll()
		res = []
		for a in accounts:
			res.append(cls(a, clientdao.ClientDAO.read(a.client_id), bankdao.BankDAO.read(a.bank_id)))
		return res
	@classmethod
	def deposit(cls, account_number, amount):
		if not isinstance(amount, decimal.Decimal):
			raise TypeError()
		if amount <= 0:
			raise ValueError()
		account = accountdao.AccountDAO.readByAccountNumber(account_number)
		account.balance += amount
		accountdao.AccountDAO.update(account)
	@classmethod
	def withdraw(cls, account_number, amount):
		if not isinstance(amount, decimal.Decimal):
			raise TypeError()
		if amount <= 0:
			raise ValueError()
		account = accountdao.AccountDAO.readByAccountNumber(account_number)
		account.balance -= amount
		accountdao.AccountDAO.update(account)