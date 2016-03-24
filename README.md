# pysql
A small utility to return mysql queries

Instantiate the object with your mysql parameters.
  `my_connection = MYSQLQueryBot(<user>,<password>,<host>,<database>)`

Connect to the database.
  `my_connection.connect()`

Load your query to find Joey (or whoever).
  `my_conection.SELECT('p.name').FROM('People p').WHERE('p.name LIKE "Joey"')`
Query to the database looks like: **SELECT p.name FROM People p WHERE p.name LIKE Joey;**

Execute the query.
  `my_connection.query()`

Query arguments persist until changed, so:

  `my_connection.SELECT('p.name').FROM('People p').WHERE('p.name LIKE "Joey"').query()`
  `my_connection.WHERE('p.name LIKE "Sally"').query()`

  would first query 
  **SELECT p.name FROM People p WHERE p.name LIKE Joey;**
  and then 
  **SELECT p.name FROM People p WHERE p.name LIKE Sally;**

  

