# connect to the SQLite data base provided
# print the columns in the orders table
# print the total spent, and total number of items bought for every user in the users table


import sqlite3

connection = sqlite3.connect("C:\\Users\\adam.shackleton\\Documents\\automation-course\\week-four\\automation.sqlite")

# each one of these assignments overwrites the last, so only the final one actually does anything
select_orders = "SELECT * FROM orders"
select_orders = """SELECT users.name, orders.id, orders.total_cost, orders.number_of_items 
                   FROM orders
                   INNER JOIN users ON orders.user_id = users.id"""

select_orders = """SELECT users.name, sum(orders.total_cost) Total, sum(orders.number_of_items) Total_Items 
                   FROM orders
                   INNER JOIN users ON orders.user_id = users.id
                   GROUP BY users.name"""
                   
cursor = connection.cursor()
cursor.execute(select_orders)
orders = cursor.fetchall()

column_names = [description[0] for description in cursor.description]
print(column_names)

for order in orders:
    print(order)
