'''
Task 1 Create SQLalchemy ORM for HR.db
Use SQLalchemy to create classes, and map those to tables in hr.db, which we used in previous lessons for homework tasks
'''

# [https://ru.wikibooks.org/wiki/SQLAlchemy]


from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker


engine = create_engine('hr.db', echo=True)

metadata = MetaData()
users_table = Table('departments', metadata,
                    Column('department_id' integer(3) primary key not null),
                    Column('depart_name' varchar(20) not null),
                    Column('manager_id' integer(3) not null),
                    Column('location_id' integer(4))
                    )

metadata.create_all(engine)


class Depart(object):
    def __init__(self, depart_name, manager_id, location_id):
        self.d_name = depart_name
        self.man_id = manager_id
        self.loc_id = location_id

    def __repr__(self):
        return "<Depart('%s','%s', '%s')>" % (self.d_name, self.man_id, self.loc_id)


mapper(Depart, departments)

Session = sessionmaker(bind=engine)
# session = Session()
