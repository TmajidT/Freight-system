import sqlite3
import orders

def manage_drivers():
    # Connect to the database
    connection = sqlite3.connect("mydatabase.db")
    cursor = connection.cursor()

    try:
        # Check if the 'drivers' table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='drivers'")
        table_exists = cursor.fetchone()

        if not table_exists:
            # Execute the CREATE TABLE statement if the table doesn't exist
            cursor.execute('''
                CREATE TABLE drivers (
                    Driver_ID INTEGER PRIMARY KEY,
                    Driver_Full_Name TEXT
                )
            ''')
            connection.commit()
            print("Table created successfully.")

        else:
            print("Table already exists.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        connection.close()


def insert_driver(driver_id, driver_full_name):
    manage_drivers()
    # Connect to the database
    connection = sqlite3.connect("mydatabase.db")
    cursor = connection.cursor()

    try:
        # Insert data into the 'drivers' table
        cursor.execute("INSERT INTO drivers (Driver_ID, Driver_Full_Name) VALUES (?, ?)", (driver_id, driver_full_name))
        connection.commit()
        print("Record added successfully.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        connection.close()


def display_all_drivers():
    # Connect to the database
    connection = sqlite3.connect("mydatabase.db")
    cursor = connection.cursor()

    try:
        # Retrieve all data from the 'drivers' table
        cursor.execute("SELECT * FROM drivers")
        records = cursor.fetchall()

        if records:
            print("All Drivers:")
            for record in records:
                print(f"Driver ID: {record[0]}, Full Name: {record[1]}")
        else:
            print("No records found in the 'drivers' table.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        connection.close()

def driver_panel():
    while True:
        print("what is your request?")
        print("1: accept new order  2: see your order  9: exit the program")
        request = int(input("   :"))
        if request == 1:
            print("here are all of the orders")
            print()
            orders.display_all_orders()
            print()
            print("Which one do you want? : ")
            order_id = input("enter order ID: ")
            driver_id = input("enter your ID: ")
            orders.update_driver_id(order_id, driver_id)
        elif request == 2:
            order_id = input("your order id: ")
            orders.display_order_by_id(order_id)
        elif request == 9:
            break