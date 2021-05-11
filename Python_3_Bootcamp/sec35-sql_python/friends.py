import sqlite3

conn = sqlite3.connect("my_friends.db")
c = conn.cursor()
# c.execute(
#     "CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")

# insert_query = "INSERT INTO friends VALUES ('Merriwether', 'Lewis', 7);"
# insert_query = '''INSERT INTO friends
#                 VALUES ('Merriwether','Lewis', 7);'''

# BAD FORM, DON'T DO THIS
# form_firstname = "Dana"
# insert_query = f"INSERT INTO FRIENDS (first_name) values ('{form_firstname}')"
# c.execute(insert_query)

# BETTER WAY!
# form_first = "Mary-Todd"
# insert_query = f"INSERT INTO friends (first_name) VALUES (?)"
# c.execute(insert_query, (form_first,))

# data = ("Steve", "Irwin", 9)
# query = "INSERT INTO friends VALUES (?,?,?)"
# c.execute(query, data)


people = [
    ("Roald", "Amundsen", 5),
    ("Rosa", "Parks", 8),
    ("Henry", "Hudson", 7),
    ("Neil", "Armstrong", 7),
    ("Daniel", "Boone", 3)]
# for person in people:
#   insert that one person


# average = 0
# for person in people:
#     c.execute("INSERT INTO friends VALUES (?,?,?)", person)
#     average += person[2]
# print(average/len(people))


# Insert all at once
# c.executemany("INSERT INTO friends VALUES (?,?,?)", people)


# c.execute("SELECT * FROM friends")
# for result in c:
#     print(result)
# # you can also use fetchall insead of using a loop
# print(c.fetchall)

c.execute("SELECT * FROM friends WHERE first_name = 'Rosa';")
print(c.fetchone)

conn.commit()
conn.close()
