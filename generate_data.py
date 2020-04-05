from sqlalchemy import create_engine
from sqlalchemy.sql import text

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime

from random import randint

metadata = MetaData()

test = Table('test_table', metadata,
     Column('id', Integer, primary_key=True),
     Column('name', String),
     Column('creation_date', DateTime, nullable=True),
)

def insert_one(conn):
    ins = test.insert().values(name=str(randint(0,99999999)))
    ins.bind = engine
    result = conn.execute(ins)
    return result.inserted_primary_key[0]

def insert_multiple(conn, items):
    result = conn.execute(test.insert(), items)
    return result

def generate_data(conection_string):
    items = []

    for i in range(500):
        items.append({
            'name': 'Name-' + str(i) + '-' + str(randint(0,99999999))
        })

    engine = create_engine(conection_string)

    with engine.connect() as conn:
        insert_multiple(conn, items)

