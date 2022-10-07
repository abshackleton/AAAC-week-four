
import sqlite3
# import mysql # mysql
# import psycopg2 # postgresql
# import pyodbc # db2, MS Access, MS SQL Server, MySQL, Oracle


import sqlite3
connection = sqlite3.connect("C:\\Users\\adam.shackleton\\Documents\\automation-course\\week-four\\automation.sqlite")

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  gender TEXT,
  nationality TEXT
);
"""
cursor = connection.cursor()
cursor.execute(create_users_table)
connection.commit()


create_users = """
INSERT INTO
  users (name, age, gender, nationality)
VALUES
  ('Andy', 35, 'male', 'Scotland'),
  ('Serena', 41, 'female', 'USA'),
  ('Emma', 19, 'female', 'England'),
  ('Nick', 27, 'male', 'Australia'),
  ('Victoria', 21, 'female', 'Belarus');
"""
cursor = connection.cursor()
cursor.execute(create_users)
connection.commit()



select_users = "SELECT name, age, gender FROM users"
cursor = connection.cursor()
cursor.execute(select_users)
users = cursor.fetchall()

for user in users:
    print(user)

column_names = [description[0] for description in cursor.description]

select_orders = "SELECT * FROM orders"
cursor = connection.cursor()
cursor.execute(select_orders)
orders = cursor.fetchall()

for order in orders:
    print(order)
