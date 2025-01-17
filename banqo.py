import sys

try:
	import mysql.connector
except Exception as error:
	print("Error: Module `mysql-connector-python` not installed")
	sys.exit(-1)

try:
	from src import config
except Exception as error:
	print("Config loading failed:", error)
	sys.exit(-1)

try:
	from src import dbsingleton
	dbsingleton.DBSingleton()
except Exception as error:
	print("Connection to DB failed:", error)
	sys.exit(-1)

from src import interface

if __name__ == "__main__":
	i = interface.Interface()
	i.start()