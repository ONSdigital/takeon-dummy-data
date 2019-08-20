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

    def build_mapped_class(self):
        # Pass global class to local variable
        orm = self.orm_class
        for i in self.data:
            # create local instance of class
            orm_inst = orm()
            for j in i.__dict__:
                if j in ("end", "start"):
                    pass
                else:
                    orm_inst.__dict__[j] = self.data.__dict__[j]
            self.insert(orm_inst)


    def insert(self, orm):
        session = self.session()
        try:
            # print("Insert ORM: {}".format(orm.__dict__))
            session.add(orm)
            session.commit()
            session.close()
            # return "Data inserted"
        except Exception as error:
            session.rollback()
            session.close()
            print(error)

        
