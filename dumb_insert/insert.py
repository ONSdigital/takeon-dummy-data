from sqlalchemy.orm import sessionmaker
from get_metadata import Metadata
from sqlalchemy import exc

class InsertData:
    def __init__(self, database, table, data, orm_class, test_env):
        engine = Metadata(test_env=test_env, table_name=table)
        engine.make_engine()
        self.session = sessionmaker(bind=engine.engine)
        self.data = data
        self.orm_class = orm_class

    def insert(self):
        session = self.session()
        orm = self.orm_class()
        for i in self.data.__dict__.keys():
            orm.__dict__[i] = self.data.__dict__[i]

        try:
            print("Insert ORM: {}".format(type(orm)))
            session.add(orm)
            session.commit()
            return "Data inserted"
        except Exception as error:
            session.rollback()
            print(error)
        
