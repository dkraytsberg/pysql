# pysql
a small utility to return mysql queries

'my_connection = MYSQLQueryBot(<user>,<password>,<host>,<database>)

my_connection.connect()

my_conection.SELECT('p.name').FROM('People p').WHERE('p.name LIKE "Joey"')

my_connection.query()'
