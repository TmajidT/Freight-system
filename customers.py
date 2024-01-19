import sqlite3

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

