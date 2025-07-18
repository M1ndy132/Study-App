import mysql.connector
from mysql.connector import Error, IntegrityError

def create_connection():
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'My$qL$cH123@@',
            database = 'StudyApp'
        )
        
        if connection.is_connected():
            mycursor = connection.cursor()
            print("Successfully connected to database")
            return connection, mycursor
        
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None, None

# Create global connection and cursor objects
connection, mycursor = create_connection()
    