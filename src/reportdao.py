from src import dbsingleton
import decimal

class ClientBalanceDAO:
	def __init__(self, first_name, last_name, email, client_number, total_balance):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.client_number = client_number
		self.total_balance = total_balance

	@property
	def first_name(self):
		return self._first_name
	@first_name.setter
	def first_name(self, val):
		if not isinstance(val, str):
			raise TypeError("first_name must be a string")
		self._first_name = val

	@property
	def last_name(self):
		return self._last_name
	@last_name.setter
	def last_name(self, val):
		if not isinstance(val, str):
			raise TypeError("last_name must be a string")
		self._last_name = val

	@property
	def email(self):
		return self._email
	@email.setter
	def email(self, val):
		if not isinstance(val, str):
			raise TypeError("email must be a string")
		self._email = val

	@property
	def client_number(self):
		return self._client_number
	@client_number.setter
	def client_number(self, val):
		if not isinstance(val, str):
			raise TypeError("client_number must be a string")
		self._client_number = val

	@property
	def total_balance(self):
		return self._total_balance
	@total_balance.setter
	def total_balance(self, val):
		if not isinstance(val, decimal.Decimal):
			raise TypeError("total_balance must be a decimal")
		self._total_balance = val

	def __str__(self):
		return self.client_number + ": " + self.first_name + " " + self.last_name + " (" + self.email + "): " + str(self.total_balance) + "$"

	@classmethod
	def readAll(cls):
		sql = "select first_name, last_name, email, client_number, total_balance from Client_Balance"
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql)
		bulk = cursor.fetchall()
		result = []
		for b in bulk:
			result.append(cls(b[0], b[1], b[2], b[3], b[4]))
		return result