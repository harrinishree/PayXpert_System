import mysql.connector

class DatabaseConnectionException(Exception):
    pass

def get_connection(config):
    try:
        conn = mysql.connector.connect(**config)
        return conn
    except mysql.connector.Error as e:
        raise DatabaseConnectionException(str(e))
