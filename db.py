import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'My$qL$cH123@@',
            database = 'StudyApp'
        )
        if connection.is_connected():
            print("Successfully connected to database")
            return connection
        
    except Error as e:
        print(f"Error connectimg to database: {e}")
        return None