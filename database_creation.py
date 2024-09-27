import mysql.connector
from mysql.connector import Error

def create_database(database_name):
    try:
        # Establish a connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your host
            user='admin',  # Replace with your username
            password='admin'  # Replace with your password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create a new database
            cursor.execute(f"CREATE DATABASE {database_name}")
            print(f"Database '{database_name}' created successfully.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    db_name = "sales"  # Replace with your desired database name
    create_database(db_name)
