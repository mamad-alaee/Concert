import sqlite3
from sqlite3 import Error

dbname = "Concert.db"


def create_tables():
    conn = None
    try:
        conn = sqlite3.connect(dbname)
        cobj = conn.cursor()
        cobj.execute(
            "CREATE TABLE Singer(id INTEGER PRIMARY KEY , name TEXT, style TEXT, age integer, gender INTEGER )")
        cobj.execute("CREATE TABLE Hall(id INTEGER PRIMARY KEY , name TEXT, amount TEXT, address TEXT)")
        cobj.execute("CREATE TABLE Concert(id INTEGER PRIMARY KEY , price INTEGER, date TEXT, start_time TEXT, "
                     "end_time TEXT,singer_id INTEGER references Singer(id),hall_id INTEGER references Hall(id))")
        conn.commit()
        print("database created")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def insert_singer(data):
    conn = None
    try:
        conn = sqlite3.connect(dbname)
        cobj = conn.cursor()
        cobj.execute("INSERT INTO Singer VALUES(?,?,?,?,?)", data)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def insert_hall(data):
    conn = None
    try:
        conn = sqlite3.connect(dbname)
        cobj = conn.cursor()
        cobj.execute("INSERT INTO Singer VALUES(?,?,?,?)", data)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def insert_concert(data):
    conn = None
    try:
        conn = sqlite3.connect(dbname)
        cobj = conn.cursor()
        cobj.execute("INSERT INTO Singer VALUES(?,?,?,?,?,?,?)", data)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def read_singer(where_filter):
    conn = None
    try:
        conn = sqlite3.connect(dbname)
        cobj = conn.cursor()
        cobj.execute("SELECT * FROM Singer" + where_filter)
        result = cobj.fetchall()
        return result
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def read_concert(where_filter):
    conn = None
    try:
        conn = sqlite3.connect(dbname)
        cobj = conn.cursor()
        cobj.execute("SELECT * FROM Concert" + where_filter)
        result = cobj.fetchall()
        return result
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def read_hall(where_filter):
    conn = None
    try:
        conn = sqlite3.connect(dbname)
        cobj = conn.cursor()
        cobj.execute("SELECT * FROM Hall" + where_filter)
        result = cobj.fetchall()
        return result
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def delete_hall(where_filter):
    conn = None
    try:
        conn = sqlite3.connect(dbname)
        cobj = conn.cursor()
        cobj.execute("DELETE FROM Hall" + where_filter)
        result = cobj.fetchall()
        return result
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def delete_concert(where_filter):
    conn = None
    try:
        conn = sqlite3.connect(dbname)
        cobj = conn.cursor()
        cobj.execute("DELETE FROM Concert" + where_filter)
        result = cobj.fetchall()
        return result
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def delete_singer(where_filter):
    conn = None
    try:
        conn = sqlite3.connect(dbname)
        cobj = conn.cursor()
        cobj.execute("DELETE FROM Singer" + where_filter)
        result = cobj.fetchall()
        return result
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
