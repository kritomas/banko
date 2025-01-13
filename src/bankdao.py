from src import dbsingleton

class BankDAO:
	def __init__(self, id, address_id, name):
		self.id = id
		self.address_id = address_id
		self.name = name

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
	def name(self):
		return self._name
	@name.setter
	def name(self, val):
		if not isinstance(val, str):
			raise TypeError()
		self._name = val

	@classmethod
	def create(cls, obj):
		if not isinstance(obj, cls):
			raise TypeError()
		sql = "insert into Bank (Address_id, name) values (%s, %s)"
		values = (obj.address_id, obj.name)
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		dbsingleton.DBSingleton().commit()
		return cls.read(cursor.lastrowid)
	@classmethod
	def read(cls, id):
		sql = "select id, Address_id, name from Bank where id=%s"
		values = (id,)
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		result = cursor.fetchone()
		return cls(result[0], result[1], result[2])
	@classmethod
	def readAll(cls):
		sql = "select id, Address_id, name from Bank"
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
		sql = "update Bank set Address_id=%s, name=%s where id=%s"
		values = (obj.address_id, obj.name, obj.id)
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