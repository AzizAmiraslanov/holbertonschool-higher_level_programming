#!/usr/bin/python3
"""Print the first State object from the database using SQLAlchemy"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Komut satırı argumentləri
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # MySQL serverinə qoşulma
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Session yaradılır
    Session = sessionmaker(bind=engine)
    session = Session()

    # İlk state obyektini əldə edirik
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()
