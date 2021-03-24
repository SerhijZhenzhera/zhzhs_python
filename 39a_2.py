'''
Task 1 Create SQLalchemy ORM for HR.db
Use SQLalchemy to create classes, and map those to tables in hr.db, which we used in previous lessons for homework tasks
'''

# [https://ru.wikibooks.org/wiki/SQLAlchemy]


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('hr.db', echo=True)

Base = declarative_base()


class Depart(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    depart_name = Column(String)
    manager_id = Column(String)
    location_id = Column(String)

    def __init__(self, depart_name, manager_id, location_id):
        self.d_name = depart_name
        self.man_id = manager_id
        self.loc_id = location_id

    def __repr__(self):
        return "<Depart('%s','%s', '%s')>" % (self.d_name, self.man_id, self.loc_id)


Base.metadata.create_all(engine)
# users_table = User.__table__
# metadata = Base.metadata


Session = sessionmaker(bind=engine)
# session = Session()
