import random, datetime, decimal, threading
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
		"""
		Transfers money between accounts. Depending on the config, you may see this function perform a Non-Repeatable Read (see documentation).
		Parameters:
		`from_number`: Number of the account to transfer from
		`to_number`: Number of the account to transfer to
		`amount`: Amount to transfer, must be a decimal
		`notes`: Notes accompanying the transfer, e.g. 'allowance', can be None
		"""
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
		cursor = dbsingleton.DBSingletonAlternative().cursor()
		cursor.execute("start transaction")
		t = threading.Thread(target=transactiondao.TransactionDAO.transfer, args=(from_number, to_number, amount, notes)) # A separate thread is required for non-repeatable reads, a deadlock occurs otherwise.
		t.start()
		account = accountdao.AccountDAO.readByAccountNumber(from_number, cursor)
		print("Account balance before: " + str(account.balance) + "$")
		account = accountdao.AccountDAO.readByAccountNumber(from_number, cursor)
		print("Account balance after: " + str(account.balance) + "$")
		cursor.execute("commit")
		t.join()
	@classmethod
	def list(cls):
		"""
		Lists all transactions.
		Returns: A list of transactions as instances of this class.
		"""
		transactions = transactiondao.TransactionDAO.readAll()
		res = []
		for t in transactions:
			res.append(cls(t, accountdao.AccountDAO.read(t.from_id), accountdao.AccountDAO.read(t.to_id)))
		return res