import mysql.connector

conn = mysql.connector.connect(user='root', password='root', database='test', host="10.98.0.85")
cursor = conn.cursor()

cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.rowcount

conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()


