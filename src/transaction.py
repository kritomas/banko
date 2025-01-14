import random, datetime, decimal
from src import transactiondao, accountdao, dbsingleton
class Transaction:
	def __init__(self, transactiondao, fromdao, todao):
		self.from_number = fromdao.account_number
		self.to_number = todao.account_number
		self.amount = transactiondao.amount
		self.notes = transactiondao.notes
		self.created_on = transactiondao.created_on

	def __str__(self):
		return self.from_number + "->" + self.to_number + ": " + str(self.amount) + "$ at " + str(self.created_on) + ": " + (self.notes if self.notes != None else "(no notes attached)")

	@classmethod
	def transfer(cls, from_number, to_number, amount, notes=None):
		account = accountdao.AccountDAO.readByAccountNumber(from_number)
		if account == None:
			raise ValueError("Sender account doesn't exist")
		account = accountdao.AccountDAO.readByAccountNumber(to_number)
		if account == None:
			raise ValueError("Recipient account doesn't exist")
		if not isinstance(amount, decimal.Decimal):
			raise TypeError("Amount must be a decimal")
		if amount <= 0:
			raise ValueError("Amount must be positive")
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute("start transaction")
		account = accountdao.AccountDAO.readByAccountNumber(from_number, cursor)
		print("Account balance before:", account.balance)
		transactiondao.TransactionDAO.transfer(from_number, to_number, amount, notes)
		account = accountdao.AccountDAO.readByAccountNumber(from_number, cursor)
		print("Account balance after:", account.balance)
		cursor.execute("commit")
		#fromacc = accountdao.AccountDAO.readByAccountNumber(from_number)
		#toacc = accountdao.AccountDAO.readByAccountNumber(to_number)
		#transaction = transactiondao.TransactionDAO(0, fromacc.id, toacc.id, d#atetime.datetime.now(), amount, toacc)
		#transaction = transactiondao.TransactionDAO.create(account)
		#return cls(transaction, fromacc, bank)
	@classmethod
	def list(cls):
		transactions = transactiondao.TransactionDAO.readAll()
		res = []
		for t in transactions:
			res.append(cls(t, accountdao.AccountDAO.read(t.from_id), accountdao.AccountDAO.read(t.to_id)))
		return res