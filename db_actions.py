import sqlite3


# TBD
class ManageDbActions:
    def __init__(self, db_table):
        self.db_table = db_table


def create_table() -> None:
    conn = sqlite3.connect('todolist.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('''CREATE TABLE todolist
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  message_id text NOT NULL, 
                  message_text text NOT NULL, 
                  priority text NOT NULL, 
                  deprecated INTEGER NOT NULL)''')
    conn.commit()
    conn.close()


# Returns all records (text) from 'todolist' table
def get_all_items() -> list:
    conn = sqlite3.connect('todolist.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('''SELECT message_text 
                 FROM todolist''')
    res = c.fetchall()
    conn.close()
    return res


# Returns all records (text) from 'todolist' table sorted in a way to shown for /list action
def get_all_items_to_display() -> list:
    conn = sqlite3.connect('todolist.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('''SELECT message_text 
                 FROM todolist 
                 WHERE deprecated=0
                 ORDER BY priority''')
    res = c.fetchall()
    conn.close()
    return res


# Adds a record to 'todolist' table
def add_item(message_id: str, text: str, priority: str, deprecated: int) -> None:
    conn = sqlite3.connect('todolist.db', check_same_thread=False)
    c = conn.cursor()

    # Re-work to autoincrement:
    c.execute('''SELECT id 
                 FROM todolist 
                 ORDER BY id 
                 DESC LIMIT 1''')
    last_id = c.fetchone()
    print(last_id)
    item_id = 1 if last_id is None else last_id[0] + 1

    c.execute(f'''INSERT INTO todolist 
                  VALUES ({item_id},'{message_id}','{text[5:]}','{priority}',{deprecated})''')
    # Re-work format to:
    # c.execute("INSERT INTO todolist VALUES (?,?,?,?)", (a, b, c, d))
    # c.execute("INSERT INTO todolist VALUES (:col1)", {'col1': a})

    conn.commit()
    conn.close()


# Returns a record with specified id
def get_item_by_id(item_id: str) -> tuple:
    conn = sqlite3.connect('todolist.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT * "
              f"FROM todolist WHERE id={item_id}")  # Re-work to use ? ?
    res = c.fetchone()
    conn.close()
    return res


# Returns all records that match 'priority' criteria
def get_items_by_priority(items_pr: str):
    conn = sqlite3.connect('todolist.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT * "
              "FROM todolist "
              f"WHERE priority='{items_pr}'")  # Re-work to use ? ?
    res = c.fetchall
    conn.close()
    return res


# Updates 'deprecated' to 1 (True) for selected record
def deprecate_list_item(item_id: str) -> None:
    conn = sqlite3.connect('todolist.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("UPDATE todolist "
              "SET deprecated=1 "
              f"WHERE id={item_id}")  # Re-work to use ? ?
    conn.commit()
    conn.close()


# Updates 'priority' to specified value for selected record
def change_priority_list_item(item_id: str, item_pr: str) -> None:
    conn = sqlite3.connect('todolist.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("UPDATE todolist "
              f"SET priority={item_pr} "
              f"WHERE id={item_id}")  # Re-work to use ? ?
    conn.commit()
    conn.close()
