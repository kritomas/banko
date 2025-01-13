from src import dbsingleton

class ClientDAO:
	def __init__(self, id, address_id, first_name, last_name, email, client_number):
		self.id = id
		self.address_id = address_id
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.client_number = client_number

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
	def first_name(self):
		return self._first_name
	@first_name.setter
	def first_name(self, val):
		if not isinstance(val, str):
			raise TypeError()
		self._first_name = val

	@property
	def last_name(self):
		return self._last_name
	@last_name.setter
	def last_name(self, val):
		if not isinstance(val, str):
			raise TypeError()
		self._last_name = val

	@property
	def email(self):
		return self._email
	@email.setter
	def email(self, val):
		if not isinstance(val, str):
			raise TypeError()
		self._email = val

	@property
	def client_number(self):
		return self._client_number
	@client_number.setter
	def client_number(self, val):
		if not isinstance(val, str):
			raise TypeError()
		self._client_number = val

	@classmethod
	def create(cls, obj):
		if not isinstance(obj, cls):
			raise TypeError()
		sql = "insert into Client (Address_id, first_name, last_name, email, client_number) values (%s, %s, %s, %s, %s)"
		values = (obj.address_id, obj.first_name, obj.last_name, obj.email, obj.client_number)
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		dbsingleton.DBSingleton().commit()
		return cls.read(cursor.lastrowid)
	@classmethod
	def read(cls, id):
		sql = "select id, Address_id, first_name, last_name, email, client_number from Client where id=%s"
		values = (id,)
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		result = cursor.fetchone()
		return cls(result[0], result[1], result[2], result[3], result[4], result[5])
	@classmethod
	def readByClientNumber(cls, client_number):
		sql = "select id, Address_id, first_name, last_name, email, client_number from Client where client_number=%s"
		values = (client_number,)
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		result = cursor.fetchone()
		return cls(result[0], result[1], result[2], result[3], result[4], result[5])
	@classmethod
	def readAll(cls):
		sql = "select id, Address_id, first_name, last_name, email, client_number from Client"
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
		sql = "update Client set Address_id=%s, first_name=%s, last_name=%s, email=%s, client_number=%s where id=%s"
		values = (obj.address_id, obj.first_name, obj.last_name, obj.email, obj.client_number, obj.id)
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		dbsingleton.DBSingleton().commit()
	@classmethod
	def delete(cls, obj):
		if not isinstance(obj, cls):
			raise TypeError()
		sql = "delete from Client where id=%s"
		values = (obj.id, )
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		dbsingleton.DBSingleton().commit()