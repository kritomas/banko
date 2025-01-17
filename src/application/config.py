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
if not "fun" in conf:
	raise ValueError("Config entry fun not found")
if not "isolation_level" in conf["fun"]:
	raise ValueError("Config entry fun.isolation_level not found")

if not isinstance(conf["db"]["host"], str):
	raise ValueError("Config entry db.host must be a string")
if not isinstance(conf["db"]["user"], str):
	raise ValueError("Config entry db.user must be a string")
if not isinstance(conf["db"]["password"], str):
	raise ValueError("Config entry db.password must be a string")
if not isinstance(conf["db"]["database"], str):
	raise ValueError("Config entry db.database must be a string")
if not conf["fun"]["isolation_level"] in ("READ UNCOMMITTED", "READ COMMITTED", "REPEATABLE READ", "SERIALIZABLE"):
	raise ValueError("Config entry fun.isolation_level must be one of: \"READ UNCOMMITTED\", \"READ COMMITTED\", \"REPEATABLE READ\", \"SERIALIZABLE\"")