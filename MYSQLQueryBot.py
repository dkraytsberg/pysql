import mysql
from mysql.connector import errorcode

class MYSQLQueryBot:

	def __init__(self, user, password, host, database):

		self.connected = False
		self.query_args = ['','','']
		
		self.db_params = {
			'user' : user,
			'password' : password,
			'host' : host,
			'database' : database
		}

	def connect(self):

		try:
			self.connection = mysql.connector.connect(**self.db_params)
			self.connected = True
		except mysql.connector.Error as e:
			print(e)
		except Exception as e:
			print("connection unsuccessful: {}".format(e))

		return self
 
	def SELECT(self, s):
		self.query_args[0] = 'SELECT ' + s
		return self

	def FROM(self, f):
		self.query_args[1] = ' FROM ' + f
		return self

	def WHERE(self, w):
		self.query_args[2] = ' WHERE ' + w
		return self

	def reset_query_args(self):
		self.query_args = ['','','']
		return self

	def query(self):
		if(not self.connected):
			return []

		query_str = ""
		for q in self.query_args:
			query_str += q

		try:
			cursor = self.connection.cursor()
		except mysql.connector.Error as e:
			print(e)
		except Exception as e:
			print("query unsuccessful: {}".format(e))
		else:
			try:
				cursor.execute(query_str)
			except mysql.connector.Error as e:
				print(e)
			else:
				results = []

				for item in cursor:
					results.append(item)

				return results
