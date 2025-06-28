import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (without specifying a database)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="belay1999%"  # Replace with your actual password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Use CREATE DATABASE IF NOT EXISTS to avoid failure if DB exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: Could not connect or create database.\nDetails: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
