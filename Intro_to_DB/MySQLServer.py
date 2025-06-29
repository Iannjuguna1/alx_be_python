# MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust user and password as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'  # Replace with your actual MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database without checking with SELECT or SHOW
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection if open
        try:
            if cursor:
                cursor.close()
            if connection.is_connected():
                connection.close()
                print("MySQL connection closed.")
        except:
            pass

if __name__ == "__main__":
    create_database()

