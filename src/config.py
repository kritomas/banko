import json

with open("config.json") as file:
	conf = json.load(file)

if not "db" in conf:
	raise ValueError("Config entry db not found")
if not "host" in conf["db"]:
	raise ValueError("Config entry db.host not found")
if not "user" in conf["db"]:
	raise ValueError("Config entry db.user not found")
if not "password" in conf["db"]:
	raise ValueError("Config entry db.password not found")
if not "database" in conf["db"]:
	raise ValueError("Config entry db.database not found")
if not isinstance(conf["db"]["host"], str):
	raise ValueError("sum: Config entry db.host must be a string")
if not isinstance(conf["db"]["user"], str):
	raise ValueError("sum: Config entry db.user must be a string")
if not isinstance(conf["db"]["password"], str):
	raise ValueError("sum: Config entry db.password must be a string")
if not isinstance(conf["db"]["database"], str):
	raise ValueError("sum: Config entry db.database must be a string")