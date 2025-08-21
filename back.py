import mysql.connector 
from mysql.connector import Error

conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Divyam@13",
        database="testdb"
)   
cursor=conn.cursor()
cursor.execute("""
               Create table fossil_Fuel(
               year int not null,
               emission varchar(250) not null,
               longitude varchar(250) not null,
               latitude varchar(250) not null)
               """)
cursor.execute("alter table fossil_fuel add column percentage_change varchar(250) not null")
conn.commit()
cursor.execute("desc fossil_fuel")
for row in cursor.fetchall():
    print(row)



