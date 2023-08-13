
import mysql.connector as sql
conn = sql.connect(host='localhost', user='root', passwd='dps123')
if conn.is_connected():
    print('Successfully connected')
c = conn.cursor()
c.execute("CREATE DATABASE IF NOT EXISTS grocery_shop")
c.execute("USE grocery_shop")
c.execute('''
    CREATE TABLE IF NOT EXISTS customer_details (
        cuid INT NOT NULL AUTO_INCREMENT,
        PRIMARY KEY(cuid),
        c_name VARCHAR(25),
        c_age INT,
        sex CHAR(7),
        phone_no INT
    )
''')
print('Customer table created')
c.execute('''
    CREATE TABLE IF NOT EXISTS product_details (
        puid INT AUTO_INCREMENT,
        PRIMARY KEY(puid),
        p_name VARCHAR(25),
        p_cost FLOAT(10),
        stock INT
    )
''')
print('Product table created')
c.execute('''
    CREATE TABLE IF NOT EXISTS worker_details (
        w_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        w_name VARCHAR(25),
        w_job VARCHAR(10),
        w_age INT,
        w_salary INT,
        phone_no INT
    )
''')
print('Worker table created')
conn.commit()
conn.close()