from src import dbsingleton

class BankDAO:
	def __init__(self, id, address_id, bank_number):
		self.id = id
		self.address_id = address_id
		self.bank_number = bank_number

	@property
	def id(self):
		return self._id
	@id.setter
	def id(self, val):
		if not isinstance(val, int):
			raise TypeError()
		self._id = val

	@property
	def address_id(self):
		return self._address_id
	@address_id.setter
	def address_id(self, val):
		if not isinstance(val, int):
			raise TypeError()
		self._address_id = val

	@property
	def bank_number(self):
		return self._bank_number
	@bank_number.setter
	def bank_number(self, val):
		if not isinstance(val, str):
			raise TypeError()
		self._bank_number = val

	@classmethod
	def create(cls, obj):
		if not isinstance(obj, cls):
			raise TypeError()
		sql = "insert into Bank (Address_id, bank_number) values (%s, %s)"
		values = (obj.address_id, obj.bank_number)
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		dbsingleton.DBSingleton().commit()
		return cls.read(cursor.lastrowid)
	@classmethod
	def read(cls, id):
		sql = "select id, Address_id, bank_number from Bank where id=%s"
		values = (id,)
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		result = cursor.fetchone()
		return cls(result[0], result[1], result[2])
	@classmethod
	def readByBankNumber(cls, bank_number):
		sql = "select id, Address_id, bank_number from Bank where bank_number=%s"
		values = (bank_number,)
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		result = cursor.fetchone()
		return cls(result[0], result[1], result[2])
	@classmethod
	def readAll(cls):
		sql = "select id, Address_id, bank_number from Bank"
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql)
		bulk = cursor.fetchall()
		result = []
		for b in bulk:
			result.append(cls(b[0], b[1], b[2]))
		return result
	@classmethod
	def update(cls, obj):
		if not isinstance(obj, cls):
			raise TypeError()
		sql = "update Bank set Address_id=%s, bank_number=%s where id=%s"
		values = (obj.address_id, obj.bank_number, obj.id)
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		dbsingleton.DBSingleton().commit()
	@classmethod
	def delete(cls, obj):
		if not isinstance(obj, cls):
			raise TypeError()
		sql = "delete from Bank where id=%s"
		values = (obj.id, )
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		dbsingleton.DBSingleton().commit()