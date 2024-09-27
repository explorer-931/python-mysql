import mysql.connector
from mysql.connector import Error

def create_table():
    try:
        # Establish a connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',       # Replace with your host
            user='admin',   # Replace with your username
            password='admin',# Replace with your password
            database='sales' # Replace with your database name
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create table SQL statement
            create_table_query = """
            CREATE TABLE products (
                id INT NOT NULL AUTO_INCREMENT,
                product_name VARCHAR(100) NOT NULL,
                price INT,
                sale_date DATE,
                PRIMARY KEY (id)
            );
            """
            cursor.execute(create_table_query)
            print("Table 'products' created successfully.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_table()
