import sqlite3

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
