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
        return "done"
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
        cobj.execute("INSERT INTO Hall VALUES(?,?,?,?)", data)
        conn.commit()
        return "done"
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
        cobj.execute("INSERT INTO Concert VALUES(?,?,?,?,?,?,?)", data)
        conn.commit()
        return "done"
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
        # cobj.execute("SELECT price,date,start_time,end_time "
        #              "FROM Concert "
        #              "INNER JOIN Singer ON Concert.singer_id = Singer.id "
        #              "INNER JOIN Hall ON Concert.hall_id = Hall.id" + where_filter)
        cobj.execute("""SELECT * FROM Concert INNER JOIN Singer ON Concert.singer_id = 
        Singer.id INNER JOIN Hall ON Concert.hall_id = Hall.id""")

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
        print("DELETE FROM Hall " + where_filter)
        cobj.execute("DELETE FROM Hall " + where_filter)
        conn.commit()
        return "done"
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
        cobj.execute("DELETE FROM Concert " + where_filter)
        conn.commit()
        return "done"
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
        cobj.execute("DELETE FROM Singer " + where_filter)
        conn.commit()
        return "done"
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def get_ids_for_combobox():
    conn = None
    try:
        conn = sqlite3.connect(dbname)
        cobj = conn.cursor()
        cobj.execute("SELECT name,id FROM Singer")
        result_singer = cobj.fetchall()
        cobj.execute("SELECT name,id FROM Hall")
        result_hall = cobj.fetchall()
        # print("this is what we got", result_hall)
        # print("this is what we got", result_singer)
        return result_hall ,result_singer
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
