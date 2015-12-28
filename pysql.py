import mysql
from mysql.connector import errorcode


def make_db_params():
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
	try:
		return mysql.connector.connect(**sql_args)
	except mysql.connector.Error as e:
		print(e)
	except Exception as e:
		print("connection unsuccessful: {}".format(e))
	else:
		print("connection successful")



def make_query(connection, query = None):
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

def main():
	sql_args = make_db_params()
	con = establish_connection(**sql_args)
	q = make_query(con)
	print(q)


if __name__ == "__main__":
	main()