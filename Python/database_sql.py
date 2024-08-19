import sqlite3

con = sqlite3.connect("library.db")

cursor = con.cursor()


def make_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS library (Name TEXT,Author TEXT,Publisher TEXT,Page_Numbers INT)")
    con.commit()


def add_data():
    cursor.execute("Insert into library Values()")
    con.commit()


def add_data2(name, author, publisher, page_numbers):
    cursor.execute("Insert into library Values(?,?,?,?)", (name, author, publisher, page_numbers))
    con.commit()


def pull_data():
    cursor.execute("Select * From library")
    list1 = cursor.fetchall()
    print("Info of Library...")
    for i in list1:
        print(i)


def pull_data2():
    cursor.execute("Select Name,Author From library")
    list1 = cursor.fetchall()
    print("Info of Library...")
    for i in list1:
        print(i)


def pull_data3(publisher):
    cursor.execute("Select * From library where Publisher = ?", (publisher,))
    list1 = cursor.fetchall()
    print("Info of Library...")
    for i in list1:
        print(i)


def updatedata(old_publisher, new_publisher):
    cursor.execute("Update library set Publisher = ? where Publisher = ?", (new_publisher, old_publisher))
    con.commit()


pull_data()
con.close()
