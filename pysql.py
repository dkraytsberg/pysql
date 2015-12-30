import mysql
from mysql.connector import errorcode


def make_db_params():
	"""
	returns a map with some default connection parameters.
	full list found at 
	https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
	"""
	user = raw_input("enter user: ")
	password = raw_input("enter password: ")
	host = raw_input("enter host: ")
	db = raw_input("enter database: ")

	args = {
		'user' : user,
		'password' : password,
		'host' : host,
		'database' : db
	}

	return args

def establish_connection(**sql_args):
	"""attempts to create a connection object from given parameters."""
	try:
		return mysql.connector.connect(**sql_args)
	except mysql.connector.Error as e:
		print(e)
	except Exception as e:
		print("connection unsuccessful: {}".format(e))



def make_query(connection, query = None):
	"""
	queries database using connection and query 
	string, prompting if no string is supplied.
	returns a list of tuples.
	"""
	try:
		cursor = connection.cursor()
	except mysql.connector.Error as e:
		print(e)
	except Exception as e:
		print("query unsuccessful: {}".format(e))
	else:
		if query == None:
			query = raw_input("enter database query: ")
		try:
			cursor.execute(query)
		except mysql.connector.Error as e:
			print(e)
		else:
			results = []

			for item in cursor:
				results.append(item)

			return results

def main(): #example usage
	sql_args = make_db_params()
	con = establish_connection(**sql_args)
	q = make_query(con)
	print(q)


if __name__ == "__main__":
	main()
