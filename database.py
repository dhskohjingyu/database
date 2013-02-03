import sqlite3
import datetime

connection = sqlite3.connect("database.sqlite")

cursor = connection.cursor()

def display_sales():
    # print the time and heading for the sales report
    now = datetime.datetime.now()
    date = (str(now.day) + "-" + str(now.month) + "-" + str(now.year))
    time = (str(now.hour) + ":" + str(now.minute))
    timestamp = "SALES REPORT AS AT " + date + " " + time

    print(timestamp)
    print("--------------------------------------------------------------------------------------")
    print("S/N  <CUSTOMER NAME in alphabetical order>     <SUBTOTAL to 2 decimal places>")

    total = 0.0
    
    #cursor.execute("SELECT * FROM customer")
    #customers = cursor.fetchall()

    # get the orders from the database
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    
    #cursor.execute("SELECT * FROM orderlines")
    #orderlines = cursor.fetchall()

    #cursor.execute("SELECT * FROM products")
    #products = cursor.fetchall()

    for order in orders:
        orderID = order[0]
        customerID = order[1]

        cursor.execute("SELECT * FROM customer WHERE CustomerID = " + customerID)
        customer = cursor.fetchall()
        print(customer[1])
        # to be continued
    
    print("--------------------------------------------------------------------------------------")
    print("TOTAL: <TOTAL to 2 decimal places>")
try:
    cursor.execute("""CREATE TABLE customer
                    (CustomerID text,
                    Name text,
                    Address text,
                    Tel text)
                      """)
    cursor.execute("""CREATE TABLE orders
                    (OrderID text,
                    CustomerID text,
                    Date text)
                      """)
    cursor.execute("""CREATE TABLE orderlines
                    (OrderID text,
                    ProductID text,
                    Quantity integer)
                      """)
    cursor.execute("""CREATE TABLE products
                    (ProductID text,
                    Description text,
                    Price real)
                      """)
    cursor.execute("INSERT INTO customer VALUES ('C001', 'Mr Ma', '1 Nanjing Avenue', '00000000')")
    cursor.execute("INSERT INTO customer VALUES ('C002', 'Mr Tan', '2 Serangoon Road', '99999999')")
    cursor.execute("INSERT INTO customer VALUES ('C003', 'Mr Toh', '3 Pasir Ris Drive', '88888888')")

    cursor.execute("INSERT INTO orders VALUES ('O001', 'C001', '30/1/13')")
    cursor.execute("INSERT INTO orders VALUES ('O002', 'C003', '31/1/13')")
    cursor.execute("INSERT INTO orders VALUES ('O003', 'C002', '1/2/13')")

    cursor.execute("INSERT INTO orderlines VALUES ('O001', 'P001', 2)")
    cursor.execute("INSERT INTO orderlines VALUES ('O002', 'P004', 500)")
    cursor.execute("INSERT INTO orderlines VALUES ('O003', 'P003', 3)")
    
    cursor.execute("INSERT INTO products VALUES ('P001', 'Strange substance, assumed to be edible until proven otherwise', 2.00)")
    cursor.execute("INSERT INTO products VALUES ('P002', 'Muffins', 1.00)")
    cursor.execute("INSERT INTO products VALUES ('P003', 'Sponge', 5.00)")
    cursor.execute("INSERT INTO products VALUES ('P004', '1 dollar bill', 2.00)")
    cursor.execute("INSERT INTO products VALUES ('P005', 'CPU', 1.23)")
except:
    print("database.sqlite already exists")

display_sales()

connection.commit()
connection.close()
