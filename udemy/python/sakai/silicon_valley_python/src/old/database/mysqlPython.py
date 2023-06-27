import mysql.connector


conn = mysql.connector.connect(host='127.0.0.1', user='root', password="")
cursor = conn.cursor()

cursor.execute(
    'CREATE DATABASE udemy_python_test_mysql_database')

conn = mysql.connector.connect(
    host='127.0.0.1',
    user="root",
    password="",
    database='udemy_python_test_mysql_database')

cursor = conn.cursor()
cursor.execute('CREATE TABLE persons('
               'id int NOT NULL AUTO_INCREMENT,'
               'name varchar(14) NOT NULL,'
               'PRIMARY KEY(id))')


cursor.execute('INSERT INTO persons(name) values("Mike") ')
cursor.execute('UPDATE persons set name="Michel" WHERE name="Mike" ')
cursor.execute('DELETE FROM persons WHERE name="Michel" ')


conn.commit()
cursor.close()
conn.close()
