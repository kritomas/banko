# Banqo - Installation

This documents contains the installation instructions for Banqo.

# Prerequisites

+	`python3`
+	`pip`
+	A MySQL server

# Database

In your favorite MySQL server, create a database and invoke all of `database/init.sql`.  
Note: If using MariaDB, the database must use the `utf8mb4` character set and the `utf8mb4_bin` collation (or any other character set and collation present in both MariaDB and mainline MySQL):

```
create database banqo character set = 'utf8mb4' collate = 'utf8mb4_bin';`
```

**The appliaction will be unable to connect otherwise.**

Then, create a user for the application to access the database. This user will need the following permissions: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `EXECUTE`

# Application

Install dependencies: `mysql-connector-python`:

```
pip install mysql-connector-python
```

In the project root, create the file `config.json` with the following format:

```
{
	"db": {
		"host": "[ip address of database server]",
		"user": "[name of user for database access]",
		"password": "[password of user for database access]",
		"database": "[name of created database]"
	},
	"fun": {
		"isolation_level": "[One of: 'READ UNCOMMITTED', 'READ COMMITTED', 'REPEATABLE READ', 'SERIALIZABLE']"
	}
}
```

See also: `doc/CONFIG.md`.

Lastly, do a test run of the appliaction:

```
python3 main.py
```

If the application gives a welcome message, everything should be ready for use ;)