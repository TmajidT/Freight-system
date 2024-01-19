import sqlite3
import orders

def connect_to_database():
    return sqlite3.connect("mydatabase.db")

def manage_customers():
    with connect_to_database() as connection:
        cursor = connection.cursor()

        try:
            # Check if the 'customers' table exists
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='customers'")
            table_exists = cursor.fetchone()

            if not table_exists:
                # Execute the CREATE TABLE statement if the table doesn't exist
                cursor.execute('''
                    CREATE TABLE customers (
                        Customer_ID INTEGER PRIMARY KEY,
                        Customer_Full_Name TEXT
                    )
                ''')
                print("Table 'customers' created successfully.")

            else:
                print("Table 'customers' already exists.")

        except Exception as e:
            print(f"Error: {e}")

def insert_customer(customer_id, customer_full_name):
    manage_customers()
    with connect_to_database() as connection:
        cursor = connection.cursor()

        try:
            # Insert data into the 'customers' table
            cursor.execute("INSERT INTO customers (Customer_ID, Customer_Full_Name) VALUES (?, ?)", (customer_id, customer_full_name))
            print("Customer record added successfully.")

        except Exception as e:
            print(f"Error: {e}")

def display_all_customers():
    with connect_to_database() as connection:
        cursor = connection.cursor()

        try:
            # Retrieve all data from the 'customers' table
            cursor.execute("SELECT * FROM customers")
            records = cursor.fetchall()

            if records:
                print("All Customers:")
                for record in records:
                    print(f"Customer ID: {record[0]}, Full Name: {record[1]}")
            else:
                print("No records found in the 'customers' table.")

        except Exception as e:
            print(f"Error: {e}")

def customers_panel():
    while True:
        print("what is your request?")
        print("1: place new order  2: see your order  9: exit the program")
        request = int(input("   :"))
        if request == 1:
            order_id = input("order ID: ")
            order_name = input("the product/order name: ")
            customer_id = input("your ID: ")
            driver_id = 0
            origin_location = input("origin location: ")
            destination = input("destination: ")
            price = input("price of the order: ")
            delivery_date = input("what is the delivery date: ")
            orders.insert_order(order_id, order_name, customer_id, driver_id, destination, origin_location, price, delivery_date)
        elif request == 2:
            order_id = input("your order id: ")
            orders.display_order_by_id(order_id)
        elif request == 9:
            break