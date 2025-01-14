from src import dbsingleton
import datetime, decimal

class TransactionDAO:
	def __init__(self, id, from_id, to_id, created_on, amount, notes = None):
		self.id = id
		self.from_id = from_id
		self.to_id = to_id
		self.created_on = created_on
		self.amount = amount
		self.notes = notes

	@property
	def id(self):
		return self._id
	@id.setter
	def id(self, val):
		if not isinstance(val, int):
			raise TypeError()
		self._id = val

	@property
	def from_id(self):
		return self._from_id
	@from_id.setter
	def from_id(self, val):
		if not isinstance(val, int):
			raise TypeError()
		self._from_id = val

	@property
	def to_id(self):
		return self._to_id
	@to_id.setter
	def to_id(self, val):
		if not isinstance(val, int):
			raise TypeError()
		self._to_id = val

	@property
	def created_on(self):
		return self._created_on
	@created_on.setter
	def created_on(self, val):
		if not isinstance(val, datetime.datetime):
			raise TypeError()
		self._created_on = val

	@property
	def amount(self):
		return self._amount
	@amount.setter
	def amount(self, val):
		if not isinstance(val, decimal.Decimal):
			raise TypeError()
		self._amount = val

	@property
	def notes(self):
		return self._notes
	@notes.setter
	def notes(self, val):
		if not isinstance(val, str) and val != None:
			raise TypeError()
		self._notes = val

	@classmethod
	def create(cls, obj):
		if not isinstance(obj, cls):
			raise TypeError()
		sql = "insert into Transaction (from_id, to_id, created_on, amount, notes) values (%s, %s, %s, %s, %s)"
		values = (obj.from_id, obj.to_id, obj.created_on, obj.amount, obj.notes)
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		dbsingleton.DBSingleton().commit()
		return cls.read(cursor.lastrowid)
	@classmethod
	def read(cls, id):
		sql = "select id, from_id, to_id, created_on, amount, notes from Transaction where id=%s"
		values = (id,)
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		result = cursor.fetchone()
		return cls(result[0], result[1], result[2], result[3], result[4], result[5])
	@classmethod
	def readAll(cls):
		sql = "select id, from_id, to_id, created_on, amount, notes from Transaction"
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql)
		bulk = cursor.fetchall()
		result = []
		for b in bulk:
			result.append(cls(b[0], b[1], b[2], b[3], b[4], b[5]))
		return result
	@classmethod
	def update(cls, obj):
		if not isinstance(obj, cls):
			raise TypeError()
		sql = "update Transaction set from_id=%s, to_id=%s, created_on=%s, amount=%s, notes=%s where id=%s"
		values = (obj.from_id, obj.to_id, obj.created_on, obj.amount, obj.notes, obj.id)
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		dbsingleton.DBSingleton().commit()
	@classmethod
	def delete(cls, obj):
		if not isinstance(obj, cls):
			raise TypeError()
		sql = "delete from Transaction where id=%s"
		values = (obj.id, )
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		dbsingleton.DBSingleton().commit()
	@classmethod
	def transfer(cls, from_number, to_number, amount, notes=None):
		sql = "call Bank_Transfer(%s, %s, %s, %s)"
		values = (from_number, to_number, amount, notes)
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		dbsingleton.DBSingleton().commit()

class TransactionOverview:
	def __init__(self, from_number, to_number, created_on, amount, notes = None):
		self.id = id
		self.from_number = from_number
		self.to_number = to_number
		self.created_on = created_on
		self.amount = amount
		self.notes = notes

	@property
	def id(self):
		return self._id
	@id.setter
	def id(self, val):
		if not isinstance(val, int):
			raise TypeError()
		self._id = val

	@property
	def from_number(self):
		return self._from_number
	@from_number.setter
	def from_number(self, val):
		if not isinstance(val, str):
			raise TypeError()
		self._from_number = val

	@property
	def to_number(self):
		return self._to_number
	@to_number.setter
	def to_number(self, val):
		if not isinstance(val, str):
			raise TypeError()
		self._to_number = val

	@property
	def created_on(self):
		return self._created_on
	@created_on.setter
	def created_on(self, val):
		if not isinstance(val, datetime.datetime):
			raise TypeError()
		self._created_on = val

	@property
	def amount(self):
		return self._amount
	@amount.setter
	def amount(self, val):
		if not isinstance(val, decimal.Decimal):
			raise TypeError()
		self._amount = val

	@property
	def notes(self):
		return self._notes
	@notes.setter
	def notes(self, val):
		if not isinstance(val, str):
			raise TypeError()
		self._notes = val

	@classmethod
	def readAll(cls):
		sql = "select from_account, to_account, created_on, amount, notes from Transactions"
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql)
		bulk = cursor.fetchall()
		result = []
		for b in bulk:
			result.append(cls(b[0], b[1], b[2], b[3], b[4]))
		return result