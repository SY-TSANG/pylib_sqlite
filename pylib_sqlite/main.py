import sqlite3

class SqliteQuery():
    def __init__(self, db):
        self.conn = sqlite3.connect(db)

    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.commit()
        self.conn.close()
    
    def fetch(self, sql):
        cursor = self.conn.cursor()
        res = cursor.execute(sql)

        return res.fetchall()
      
class PylibSqlite():
    def __init__(self, db=""):
        self.db = db

    def init(self):
        return SqliteQuery(self.db)
