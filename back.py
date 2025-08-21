import mysql.connector 
from mysql.connector import Error
def insertion(year,emision,longitude,latitude,percentage_change,change1):
    query = "insert into fossil_fuel(year,emision,longitude,latitude,change,percentage_change) values(%s,%s,%s,%s,%s,%s)"
    cursor.execute("query,(year,emision,lon,lat,change,pct_change)")
    conn.commit()
def getdata(s="hi"):
    cursor.execute("")
    
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
cursor.execute("alter table fossil_fuel add column change1 float(5,2) not null")
cursor.execute("alter table fossil_fuel change year year1 year")
conn.commit()
cursor.execute("desc fossil_fuel")
for row in cursor.fetchall():
    print(row)



