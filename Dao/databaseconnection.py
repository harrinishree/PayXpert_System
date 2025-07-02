import mysql.connector
from util.DBPropertyUtil import get_db_config

class DatabaseContext:
    def __init__(self):
        self.config = get_db_config()
        self.conn = None

    def connect(self):
        if not self.conn or not self.conn.is_connected():
            self.conn = mysql.connector.connect(**self.config)
        return self.conn

    def disconnect(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()

    def get_connection(self):
        return self.connect()
