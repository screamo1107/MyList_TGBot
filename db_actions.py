import sqlite3


# Create / re-create?
conn = sqlite3.connect('../todolist.db', check_same_thread=False)


def create_table() -> None:
    c = conn.cursor()
    c.execute('''CREATE TABLE todolist
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  message_id text NOT NULL, 
                  message_text text NOT NULL, 
                  priority text NOT NULL, 
                  deprecated INTEGER NOT NULL)''')
    conn.commit()
    conn.close()


def get_all_items() -> list:
    c = conn.cursor()
    c.execute('''SELECT message_text FROM todolist''')
    res = c.fetchall()
    # conn.close()
    return res


def add_item(message_id: str, text: str, priority: str, deprecated: int) -> None:
    c = conn.cursor()

    # Re-work to autoincrement:
    c.execute('''SELECT id FROM todolist ORDER BY id DESC LIMIT 1''')
    last_id = c.fetchone()
    print(last_id)
    item_id = 1 if last_id is None else last_id[0] + 1

    c.execute(f'''INSERT INTO todolist 
                VALUES ({item_id},'{message_id}','{text}','{priority}',{deprecated})''')
    # Re-work format to:
    # c.execute("INSERT INTO todolist VALUES (?,?,?,?)", (a, b, c, d))
    # c.execute("INSERT INTO todolist VALUES (:col1)", {'col1': a})

    conn.commit()
    # conn.close()


def get_item_by_id(item_id: str) -> tuple:
    c = conn.cursor()
    c.execute(f"SELECT * FROM todolist WHERE id={item_id}")  # Re-work to use ? ?
    res = c.fetchone()
    conn.close()
    return res


# TBD
class ManageDbActions:
    def __init__(self, db_table):
        self.db_table = db_table


# create_table()
# add_item('32312323', 'Te222xt', 'P3', 1)
# print(get_all_items())
# print(get_item_by_id('1'))
