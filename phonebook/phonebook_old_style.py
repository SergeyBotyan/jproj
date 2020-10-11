import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql import select, and_
from sqlalchemy import create_engine

Base = declarative_base()
#from creds import LOGIN, PASSS

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table users
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    l_name = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    phones = relationship("Phone", back_populates="human")

class Phone(Base):
    __tablename__ = 'phone'
    # Here we define columns for the table cars.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    phone = Column(String(250))
    phone_type = Column(String(250))
    user_id = Column(Integer, ForeignKey('people.id'))
    human = relationship("People", back_populates="phones")


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///123.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def add_people():
    l_n = input('Give the last name ')
    n = input('Give the name ')
    newpeople = People(l_name = l_n, name = n)
    session.add(newpeople)
    session.commit()
    wait = input('Введите любой символ для продолжения')

def add_phone():
    p_number = input('Give the phone number ')
    p_type = input('Give phone type ')
    p_user = input('Give the user ID ')
    phone_row = Phone(phone = p_number, phone_type = p_type, \
                user_id = p_user)
    session.add(phone_row)
    session.commit()
    wait = input('Введите любой символ для продолжения')

def update_people():
    num = input('Give the number 2 UPDATE ')
    up = session.query(People).get(num)
    l_n = input('Give the NEW last name ')
    n = input('Give the NEW name ')
    up.name = n 
    up.l_name = l_n
    session.commit()
    wait = input('Введите любой символ для продолжения')

def update_phone():
    num = input('Какой номер телефона изменить? ')
    up = session.query(Phone).get(num)
    ph = input('Введите новый номер телефона ')
    ph_t = input('Введите новый тип телефона ')
    up.phone = ph 
    up.phone_type = ph_t
    session.commit()
    wait = input('Готово. Введите любой символ для продолжения')

def print_all():
    s = select([People, Phone]).where(\
    People.id == Phone.user_id)
    result = session.execute(s)
    for i in result:
        print(i.l_name, i.name, i.phone, i.phone_type)
    wait = input('Введите любой символ для продолжения')

def print_result():
    n = input('Введите фамилию для отображения')
    s = select([People, Phone]).where(and_ \
    (People.id == Phone.user_id,People.l_name == n))
    result = session.execute(s)
    for i in result:
        print(i.l_name, i.name, i.phone, i.phone_type)
    wait = input('Введите любой символ для продолжения')

def delete_people():
    n = input('Введите порядкоый № для удаления ')
    del_people = session.query(People).filter(People.id == n).delete()
    session.commit()
    wait = input('Введите любой символ для продолжения')

def delete_phone():
    n = input('Введите порядкоый № для удаления ')
    del_pрщту = session.query(Phone).filter(Phone.id == n).delete()
    session.commit()
    wait = input('Введите любой символ для продолжения')

#menu loop
operation = 10
while operation != 0:
    operation = int(input(
    'Добро пожаловать в телефонный справочник! \n'
    '========================================= \n'
    'Выберите, что вы хотите сделать: \n'
    '1. Показать все записи \n'
    '2. Показать информацию о человеке \n'
    '3. Создать запись человека \n'
    '4. Создать запись телефона \n'
    '5. Обновить запись человека \n'
    '6. Обновить запись телефона \n'
    '7. Удалить запись человека \n'
    '8. Удалить запись телефона \n'
    '0. Выход из программы \n'))
    if operation == 1:
        clear_screen()
        print_all()
        clear_screen()
    elif operation == 2:
        clear_screen()
        print_result()
        clear_screen()
    elif operation == 3:
        clear_screen()
        add_people()
        clear_screen()
    elif operation == 4:
        clear_screen()
        add_phone()
        clear_screen()
    elif operation == 5:
        clear_screen()
        update_people()
        clear_screen()
    elif operation == 6:
        update_phone()
    elif operation == 7:
        clear_screen()
        delete_people()
        clear_screen()
    elif operation == 8:
        clear_screen()
        delete_phone()
        clear_screen()
    else:
        continue
    if operation == 0:
        break  

#the end
clear_screen()
session.commit()
session.close()  
print('Спасибо за работу!')