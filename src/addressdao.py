from src import dbsingleton

class AddressDAO:
	def __init__(self, id, city, street, house_number, additional=None):
		self.id = id
		self.city = city
		self.street = street
		self.house_number = house_number
		self.additional = additional

	@property
	def id(self):
		return self._id
	@id.setter
	def id(self, val):
		if not isinstance(val, int):
			raise TypeError()
		self._id = val

	@property
	def city(self):
		return self._city
	@city.setter
	def city(self, val):
		if not isinstance(val, str):
			raise TypeError()
		self._city = val

	@property
	def street(self):
		return self._street
	@street.setter
	def street(self, val):
		if not isinstance(val, str):
			raise TypeError()
		self._street = val

	@property
	def house_number(self):
		return self._house_number
	@house_number.setter
	def house_number(self, val):
		if not isinstance(val, str):
			raise TypeError()
		self._house_number = val

	@property
	def additional(self):
		return self._additional
	@additional.setter
	def additional(self, val):
		if not isinstance(val, str) and val != None:
			raise TypeError()
		self._additional = val

	@classmethod
	def create(cls, obj):
		if not isinstance(obj, cls):
			raise TypeError()
		sql = "insert into Address (city, street, house_number, additional) values (%s, %s, %s, %s)"
		values = (obj.city, obj.street, obj.house_number, obj.additional)
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		dbsingleton.DBSingleton().commit()
		return cls.read(cursor.lastrowid)
	@classmethod
	def read(cls, id):
		sql = "select id, city, street, house_number, additional from Address where id=%s"
		values = (id,)
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		result = cursor.fetchone()
		return cls(result[0], result[1], result[2], result[3], result[4])
	@classmethod
	def readAll(cls):
		sql = "select id, city, street, house_number, additional from Address"
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql)
		bulk = cursor.fetchall()
		result = []
		for b in bulk:
			result.append(cls(b[0], b[1], b[2], b[3], b[4]))
		return result
	@classmethod
	def update(cls, obj):
		if not isinstance(obj, cls):
			raise TypeError()
		sql = "update Address set city=%s, street=%s, house_number=%s, additional=%s where id=%s"
		values = (obj.city, obj.street, obj.house_number, obj.additional, obj.id)
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		dbsingleton.DBSingleton().commit()
	@classmethod
	def delete(cls, obj):
		if not isinstance(obj, cls):
			raise TypeError()
		sql = "delete from Address where id=%s"
		values = (obj.id, )
		cursor = dbsingleton.DBSingleton().cursor()
		cursor.execute(sql, values)
		dbsingleton.DBSingleton().commit()