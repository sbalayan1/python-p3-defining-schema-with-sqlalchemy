#!/usr/bin/env python3

from sqlalchemy import Table, Column, Integer, String, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())


if __name__ == '__main__':
    engine = create_engine("sqlite:///students.db")
    Base.metadata.create_all(engine)



###The code below does the exact samething as the code above and below
    # from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine

    # metadata_obj = MetaData()

    # students = Table(
    #     "students",
    #     metadata_obj,
    #     Column("id", Integer(), primary_key=True),
    #     Column("name", String())
    # )

    # if __name__ == '__main__':
    #     engine = create_engine("sqlite:///students.db")
    #     metadata_obj.create_all(engine)



###The code does the same as the two above. Instead of using the metadata_obj and the create_all method, we directly call the create method ON the students Table instance. 

    # metadata_obj = MetaData()

    # students = Table(
    #     "students",
    #     metadata_obj,
    #     Column("id", Integer(), primary_key=True),
    #     Column("name", String())
    # )


    # if __name__ == '__main__':
    #     engine = create_engine("sqlite:///students.db")
    #     students.create(engine)