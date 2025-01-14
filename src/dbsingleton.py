import mysql.connector
from src import config

class DBSingleton:
	connection = None

	def __new__(cls):
		if cls.connection == None:
			cls._connect()
		return cls.connection

	@classmethod
	def _connect(cls):
		cls.connection = mysql.connector.connect(
			host=config.conf["db"]["host"],
			user=config.conf["db"]["user"],
			password=config.conf["db"]["password"],
			database=config.conf["db"]["database"],
			charset="utf8mb4", # Workaround for MariaDB
			collation="utf8mb4_bin" # Workaround for MariaDB
		)
		cursor = cls.connection.cursor()
		cursor.execute("set session transaction isolation level " + config.conf["fun"]["isolation_level"])
		cls.connection.commit()
	@classmethod
	def close(cls):
		cls.connection.close()
		cls.connection = None

class DBSingletonAlternative: # MySQl doesn't support transaction nesting, so an entire connection is required.
	connection = None

	def __new__(cls):
		if cls.connection == None:
			cls._connect()
		return cls.connection

	@classmethod
	def _connect(cls):
		cls.connection = mysql.connector.connect(
			host=config.conf["db"]["host"],
			user=config.conf["db"]["user"],
			password=config.conf["db"]["password"],
			database=config.conf["db"]["database"],
			charset="utf8mb4", # Workaround for MariaDB
			collation="utf8mb4_bin" # Workaround for MariaDB
		)
		cursor = cls.connection.cursor()
		cursor.execute("set session transaction isolation level " + config.conf["fun"]["isolation_level"])
		cls.connection.commit()
	@classmethod
	def close(cls):
		cls.connection.close()
		cls.connection = None