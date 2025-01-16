import random, datetime, decimal
from src import accountdao, clientdao, bankdao

ACCOUNT_TYPES = ("basic", "savings")

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
		"""
		Opens a new account.
		Parameters:
		`client_number`: Number of the owner
		`bank_number`: Number of the bank to manage the account
		`account_type`: One of: 'basic', 'savings'
		Returns: The newly created account as an instance of this class.
		"""
		client = clientdao.ClientDAO.readByClientNumber(client_number)
		if client == None:
			raise ValueError("That client doesn't exist")
		bank = bankdao.BankDAO.readByBankNumber(bank_number)
		if bank == None:
			raise ValueError("That bank doesn't exist")
		if not account_type in ACCOUNT_TYPES:
			raise ValueError("Unknown account type")
		account = accountdao.AccountDAO(0, client.id, bank.id, account_type, str(random.randint(100000000000, 999999999999)), False, datetime.datetime.now(), decimal.Decimal(0))
		account = accountdao.AccountDAO.create(account)
		return cls(account, client, bank)
	@classmethod
	def close(cls, account_number):
		"""
		Closes an account.
		Parameters:
		`account_number`: Number of the account to close.
		Returns: The just-closed account as an instance of this class.
		"""
		account = accountdao.AccountDAO.readByAccountNumber(account_number)
		if account == None:
			raise ValueError("That account doesn't exist")
		accountdao.AccountDAO.delete(account)
		return account
	@classmethod
	def list(cls):
		"""
		Lists all accounts.
		Returns: A list of all accounts as instances of this class.
		"""
		accounts = accountdao.AccountDAO.readAll()
		res = []
		for a in accounts:
			res.append(cls(a, clientdao.ClientDAO.read(a.client_id), bankdao.BankDAO.read(a.bank_id)))
		return res
	@classmethod
	def deposit(cls, account_number, amount):
		"""
		Deposits money into an account.
		Parameters:
		`account_number`: Number of the account to deposit into.
		`amount`: The amount of deposit. Must be a decimal.
		"""
		if not isinstance(amount, decimal.Decimal):
			raise TypeError("Amount must be a decimal")
		if amount <= 0:
			raise ValueError("Amount must be positive")
		account = accountdao.AccountDAO.readByAccountNumber(account_number)
		if account == None:
			raise ValueError("That account doesn't exist")
		account.balance += amount
		accountdao.AccountDAO.update(account)
	@classmethod
	def withdraw(cls, account_number, amount):
		"""
		Withdraws money from an account.
		Parameters:
		`account_number`: Number of the account to withdraw from.
		`amount`: The amount of withdraw. Must be a decimal.
		"""
		if not isinstance(amount, decimal.Decimal):
			raise TypeError("Amount must be a decimal")
		if amount <= 0:
			raise ValueError("Amount must be positive")
		account = accountdao.AccountDAO.readByAccountNumber(account_number)
		if account == None:
			raise ValueError("That account doesn't exist")
		account.balance -= amount
		accountdao.AccountDAO.update(account)