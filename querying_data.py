import mysql.connector
from mysql.connector import Error

def filter_products_by_price(min_price, max_price):
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

            # SQL query to filter products by price range
            query = """
            SELECT * FROM sales_data 
            WHERE price BETWEEN %s AND %s
            """
            cursor.execute(query, (min_price, max_price))
            records = cursor.fetchall()

            # Print the results
            print(f"Products with price between {min_price} and {max_price}:")
            for row in records:
                print(f"ID: {row[0]}, Product Name: {row[1]}, Price: {row[2]}, Sale Date: {row[3]}")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    min_price = 100
    max_price = 400
    filter_products_by_price(min_price, max_price)
