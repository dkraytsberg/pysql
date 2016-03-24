# pysql
***
A small utility to return mysql queries


`my_connection = MYSQLQueryBot(<user>,<password>,<host>,<database>)`
`my_connection.connect()`
`my_conection.SELECT('p.name').FROM('People p').WHERE('p.name LIKE "Joey"')`

**SELECT p.name FROM People p WHERE p.name LIKE Joey;**

`my_connection.query()`
***
Query arguments persist until changed

`my_connection.SELECT('p.name').FROM('People p').WHERE('p.name LIKE "Joey"').query()`
`my_connection.WHERE('p.name LIKE "Sally"').query()`

**SELECT p.name FROM People p WHERE p.name LIKE Joey;**

**SELECT p.name FROM People p WHERE p.name LIKE Sally;**

  

