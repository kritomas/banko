import datetime, decimal
from src import dbsingleton

class AccountDAO:
	def __init__(self, id, client_id, bank_id, account_type, account_number, is_frozen, created_on, balance):
		self.id = id
		self.client_id = client_id
		self.bank_id = bank_id
		self.account_type = account_type
		self.account_number = account_number
		self.is_frozen = is_frozen
		self.created_on = created_on
		self.balance = balance

	@property
	def id(self):
		return self._id
	@id.setter
	def id(self, val):
		if not isinstance(val, int):
			raise TypeError()
		self._id = val

	@property
	def client_id(self):
		return self._client_id
	@client_id.setter
	def client_id(self, val):
		if not isinstance(val, int):
			raise TypeError()
		self._client_id = val

	@property
	def bank_id(self):
		return self._bank_id
	@bank_id.setter
	def bank_id(self, val):
		if not isinstance(val, int):
			raise TypeError()
		self._bank_id = val

	@property
	def account_type(self):
		return self._account_type
	@account_type.setter
	def account_type(self, val):
		if not isinstance(val, str):
			raise TypeError()
		self._account_type = val

	@property
	def account_number(self):
		return self._account_number
	@account_number.setter
	def account_number(self, val):
		if not isinstance(val, str):
			raise TypeError()
		self._account_number = val

	@property
	def is_frozen(self):
		return self._is_frozen
	@is_frozen.setter
	def is_frozen(self, val):
		if not isinstance(val, bool):
			raise TypeError()
		self._is_frozen = val

	@property
	def created_on(self):
		return self._created_on
	@created_on.setter
	def created_on(self, val):
		if not isinstance(val, datetime.datetime):
			raise TypeError()
		self._created_on = val

	@property
	def balance(self):
		return self._balance
	@balance.setter
	def balance(self, val):
		if not isinstance(val, decimal.Decimal):
			raise TypeError()
		self._balance = val

	@classmethod
	def create(cls, obj):
		if not isinstance(obj, cls):
			raise TypeError()
		sql = "insert into Account (Client_id, Bank_id, account_type, account_number, is_frozen, created_on, balance) values (%s, %s, %s, %s, %s, %s, %s)"
		values = (obj.client_id, obj.bank_id, obj.account_type, obj.account_number, obj.is_frozen, obj.created_on, obj.balance)
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		dbsingleton.DBSingleton().commit()
		return cls.read(cursor.lastrowid)
	@classmethod
	def read(cls, id):
		sql = "select id, Client_id, Bank_id, account_type, account_number, is_frozen, created_on, balance from Account where id=%s"
		values = (id,)
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		result = cursor.fetchone()
		return cls(result[0], result[1], result[2], result[3], result[4], bool(result[5]), result[6], result[7])
	@classmethod
	def readAll(cls):
		sql = "select id, Client_id, Bank_id, account_type, account_number, is_frozen, created_on, balance from Account"
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql)
		bulk = cursor.fetchall()
		result = []
		for b in bulk:
			result.append(cls(b[0], b[1], b[2], b[3], b[4], bool(b[5]), b[6], b[7]))
		return result
	@classmethod
	def update(cls, obj):
		if not isinstance(obj, cls):
			raise TypeError()
		sql = "update Account set Client_id=%s, Bank_id=%s, account_type=%s, account_number=%s, is_frozen=%s, created_on=%s, balance=%s where id=%s"
		values = (obj.client_id, obj.bank_id, obj.account_type, obj.account_number, obj.is_frozen, obj.created_on, obj.balance, obj.id)
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		dbsingleton.DBSingleton().commit()
	@classmethod
	def delete(cls, obj):
		if not isinstance(obj, cls):
			raise TypeError()
		sql = "delete from Account where id=%s"
		values = (obj.id, )
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		dbsingleton.DBSingleton().commit()