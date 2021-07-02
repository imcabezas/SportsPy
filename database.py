import sqlite3
from sqlite3.dbapi2 import Cursor


class Database(object):

    dbName = 'sports.db'
    __singleton = None
    conn = None
    cursor = None

    @property
    def __new__(cls):
        if Database.__singleton is None:
            Database.__singleton = object.__new__(cls)
        return Database.__singleton

    @property
    def executeSchema(self):
        self.dbName
        sqlUser = "CREATE TABLE IF NOT EXISTS user ( id INTEGER, login TEXT, first TEXT, last TEXT)"
        self.cursor.execute(sqlUser)
        print("schema ok")
        return

    @property
    def __init__(self):
        conn = sqlite3.connect(self.dbName)
        cursor = conn.cursor()
        self.executeSchema()
