import psycopg2


def create():
    conn = psycopg2.connect(dbname="postgres",host="localhost",port="5432")
    cur = conn.cursor()

    cur.execute('''CREATE TABLE student(ID SERIAL, NAME TEXT, AGE TEXT, ADDRESS TEXT);''')
    print("table created")

    conn.commit()
    conn.close()
    print("conn closed")

def insert_data():
    conn = psycopg2.connect(dbname="postgres",host="localhost",port="5432")
    cur = conn.cursor()
    name = input("enter name ")
    age = input("enter age ")
    address = input("enter address ")

    query = '''INSERT INTO student(NAME, AGE , ADDRESS ) VALUES (%s, %s, %s);'''
    cur.execute(query,(name,age,address))
    print("data inserted")

    conn.commit()
    conn.close()
    print("conn closed")


insert_data()
