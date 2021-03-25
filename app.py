import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
 
Base = declarative_base()

class User(Base):
        __tablename__ = 'users'

        id = Column(Integer, primary_key=True)
        name = Column(String)
        



engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(blind=engine)
session = sessionmaker(blind=engine)

session = session()

user = user()
user.id = 0
user.name = "krishna"

session.add(user)
session.commit()

session.close()