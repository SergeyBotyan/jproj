from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sql_al import People, Phone, Base

# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
# Insert a User in the users table
def add_people(l_n, n): 
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind = engine)
    session = DBSession()
    people_row = People(l_name = l_n, name = n)
    session.add(people_row)
    session.commit()

def add_phones(ph, ph_t): 
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    phone_row = Phone(phone = ph, phone_type = ph_t)
    session.add(phone_row)
    session.commit()