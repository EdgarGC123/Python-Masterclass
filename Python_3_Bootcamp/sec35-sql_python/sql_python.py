import sqlite3

conn = sqlite3.connect("my_friends.db")

"CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER"

conn.close()
