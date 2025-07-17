from db import create_connection

def test_database_connection():
    with create_connection() as connection:
        assert connection.is_connected()