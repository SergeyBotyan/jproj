from sqlalchemy import create_engine
from sql_al import Users, Base, Cars
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# person = session.query(Users).first()
# users = session.query(Users).filter(Users.id>=4).delete()