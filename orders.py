import sqlite3

def connect_to_database():
    return sqlite3.connect("mydatabase.db")

def manage_orders():
    with connect_to_database() as connection:
        cursor = connection.cursor()

        try:
            # Check if the 'orders' table exists
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='orders'")
            table_exists = cursor.fetchone()

            if not table_exists:
                # Execute the CREATE TABLE statement if the table doesn't exist
                cursor.execute('''
                    CREATE TABLE orders (
                        Order_ID INTEGER PRIMARY KEY,
                        Customer_ID INTEGER NOT NULL,
                        Driver_ID INTEGER,
                        Order_Destination TEXT,
                        Order_Origin_Loc TEXT,
                        Order_Price INTEGER,
                        Order_Delivery_Date DATE,
                        FOREIGN KEY (Customer_ID) REFERENCES customers(Customer_ID),
                        FOREIGN KEY (Driver_ID) REFERENCES drivers(Driver_ID)
                    )
                ''')
                print("Table 'orders' created successfully.")

            else:
                print("Table 'orders' already exists.")

        except Exception as e:
            print(f"Error: {e}")

def insert_order(order_id, customer_id, driver_id, destination, origin_loc, price, delivery_date):
    manage_orders()
    with connect_to_database() as connection:
        cursor = connection.cursor()

        cursor = connection.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        connection.commit()

        try:
            # Insert data into the 'orders' table
            cursor.execute("INSERT INTO orders (Order_ID, Customer_ID, Driver_ID, Order_Destination, Order_Origin_Loc, Order_Price, Order_Delivery_Date) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (order_id, customer_id, driver_id, destination, origin_loc, price, delivery_date))
            print("Order record added successfully.")

        except Exception as e:
            print(f"Error: {e}")

def display_all_orders():
    with connect_to_database() as connection:
        cursor = connection.cursor()

        try:
            # Retrieve all data from the 'orders' table
            cursor.execute("SELECT * FROM orders")
            records = cursor.fetchall()

            if records:
                print("All Orders:")
                for record in records:
                    print(f"Order ID: {record[0]}, Customer ID: {record[1]}, Driver ID: {record[2]}, Destination: {record[3]}, Origin Location: {record[4]}, Price: {record[5]}, Delivery Date: {record[6]}")
            else:
                print("No records found in the 'orders' table.")

        except Exception as e:
            print(f"Error: {e}")


def display_order_by_id(order_id):
    with connect_to_database() as connection:
        cursor = connection.cursor()

        try:
            # Retrieve data for a specific order by Order_ID
            cursor.execute("SELECT * FROM orders WHERE Order_ID=?", (order_id,))
            record = cursor.fetchone()

            if record:
                print(f"Order ID: {record[0]}, Customer ID: {record[1]}, Driver ID: {record[2]}, Destination: {record[3]}, Origin Location: {record[4]}, Price: {record[5]}, Delivery Date: {record[6]}")
            else:
                print(f"No record found for Order ID {order_id}.")

        except Exception as e:
            print(f"Error: {e}")
