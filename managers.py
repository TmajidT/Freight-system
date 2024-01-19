import sqlite3

import customers
import drivers
import orders

def connect_to_database():
    return sqlite3.connect("mydatabase.db")

def manage_managers():
    with connect_to_database() as connection:
        cursor = connection.cursor()

        try:
            # Check if the 'managers' table exists
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='managers'")
            table_exists = cursor.fetchone()

            if not table_exists:
                # Execute the CREATE TABLE statement if the table doesn't exist
                cursor.execute('''
                    CREATE TABLE managers (
                        Manager_ID INTEGER PRIMARY KEY,
                        Manager_Full_Name TEXT
                    )
                ''')
                print("Table 'managers' created successfully.")

            else:
                print("Table 'managers' already exists.")

        except Exception as e:
            print(f"Error: {e}")

def insert_manager(manager_id, manager_full_name):
    manage_managers()
    with connect_to_database() as connection:
        cursor = connection.cursor()

        try:
            # Insert data into the 'managers' table
            cursor.execute("INSERT INTO managers (Manager_ID, Manager_Full_Name) VALUES (?, ?)", (manager_id, manager_full_name))
            print("Manager record added successfully.")

        except Exception as e:
            print(f"Error: {e}")

def display_all_managers():
    with connect_to_database() as connection:
        cursor = connection.cursor()

        try:
            # Retrieve all data from the 'managers' table
            cursor.execute("SELECT * FROM managers")
            records = cursor.fetchall()

            if records:
                print("All Managers:")
                for record in records:
                    print(f"Manager ID: {record[0]}, Full Name: {record[1]}")
            else:
                print("No records found in the 'managers' table.")

        except Exception as e:
            print(f"Error: {e}")


def manager_panel():
    while True:
        print("what is your request?")
        print("1: see customers   2: add customer   3: see order   4: see drivers   5: add driver   6: see managers   7: add manager  9: exit the program")
        request = int(input("   :"))
        if request == 1:
            print("here are all of the customers")
            print()
            customers.display_all_customers()
        elif request == 2:
            customer_id = input("enter customer ID: ")
            customer_full_name = input("enter customer's full name: ")
            customers.insert_customer(customer_id, customer_full_name)
        elif request == 3:
            print("here are all of the orders")
            print()
            orders.display_all_orders()
        elif request == 4:
            print("here are all of the drivers")
            print()
            drivers.display_all_drivers()
        elif request == 5:
            driver_id = input("enter driver's ID: ")
            driver_full_name = input("enter driver's full name: ")
            drivers.insert_driver(driver_id, driver_full_name)
        elif request == 6:
            print("here are all of the managers")
            print()
            display_all_managers()
        elif request == 7:
            manager_id = input("enter manager ID: ")
            manager_full_name = input("enter manager's full name: ")
            insert_manager(manager_id, manager_full_name)
        elif request == 9:
            break