from sqlalchemy import Boolean, Column, create_engine, Integer, MetaData, Table, String


engine = create_engine('sqlite:///todolist.db', echo=True)
meta = MetaData()

todo_list = Table('Todo_list', meta,
                  Column('id', Integer, primary_key=True),
                  Column('message_id', String),
                  Column('text', String),
                  Column('priority', String),
                  Column('deprecated', Boolean)
                  )

meta.create_all(engine)
# TBD: Run at the beginning somehow
