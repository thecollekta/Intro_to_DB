# MySQLServer.py

import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

def main():
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',    # Replace with your host if it's not localhost
            user='root',         # Replace with your MySQL username
            password='admin@123.'  # Replace with your MySQL password
        )
        
        if connection.is_connected():
            print("Successfully connected to MySQL server")
            cursor = connection.cursor()
            
            # Create the database
            create_database(cursor)
            
            # Close cursor and connection
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

if __name__ == "__main__":
    main()