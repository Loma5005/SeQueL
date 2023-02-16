import sqlite3
conn=sqlite3.connect('emobilis.db')
print("opened db successfully")

conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES(1,'Lynton',18,'emobilis')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES(2,'Mark',18,'emobilis')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES(3,'Ethan',18,'SDA')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES(4,'Ambrose',18,'Pettans')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES(5,'Greg',18,'Strathmore')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES(6,'Beavon',18,'Army')")

conn.commit()
print("records added successfuly")
conn.close()