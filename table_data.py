import mysql.connector
from mysql.connector import Error

def insert_data():
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

            # Insert data into the table
            insert_query = """
            INSERT INTO sales_data (product_name, price, sale_date) VALUES (%s, %s, %s)
            """
            records = [
                ('Product 1', 100, '2023-01-01'),
                ('Product 2', 150, '2023-01-02'),
                ('Product 3', 200, '2023-01-03'),
                ('Product 4', 250, '2023-01-04'),
                ('Product 5', 300, '2023-01-05'),
                ('Product 6', 350, '2023-01-06'),
                ('Product 7', 400, '2023-01-07'),
                ('Product 8', 450, '2023-01-08'),
                ('Product 9', 500, '2023-01-09'),
                ('Product 10', 550, '2023-01-10')
            ]
            cursor.executemany(insert_query, records)
            connection.commit()  # Commit the changes
            print("10 records inserted successfully.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    insert_data()
