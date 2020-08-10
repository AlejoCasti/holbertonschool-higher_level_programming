#!/usr/bin/python3
''' Script that lists all states form database '''
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]))
    sesion = sessionmaker(bind=engine)
    session = sesion()
    new_state = State(name='California')
    new_city = City(name='San Francisco', state=new_state)
    session.add(new_city)
    session.commit()
    session.close()

