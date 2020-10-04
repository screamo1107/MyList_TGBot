import sqlite3


# Create DB externally?

conn = sqlite3.connect('todolist.db')


def create_table():
    c = conn.cursor()
    c.execute('''CREATE TABLE todolist
                 (message_id text, message_text text, priority text, deprecated real)''')

    # Insert a row of data
    c.execute("INSERT INTO todolist VALUES ('123','321','P2',0)")

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


def get_all_items():
    c = conn.cursor()
    c.execute('''SELECT * FROM todolist WHERE id=:id''', {'id': 1})
    print(c.fetchall())


def add_item():
    conn = sqlite3.connect('todolist.db')
    c = conn.cursor()
    c.execute("INSERT INTO todolist VALUES ('123','321','132',True)")
    c.execute("INSERT INTO todolist VALUES (?,?,?,?)", (a, b, c, d))
    c.execute("INSERT INTO todolist VALUES (:col1)", {'col1': a})
    conn.commit()
    conn.close()



# TBD
class ManageDbActions:
    def __init__(self, db_table):
        self.db_table = db_table


get_all_items()
