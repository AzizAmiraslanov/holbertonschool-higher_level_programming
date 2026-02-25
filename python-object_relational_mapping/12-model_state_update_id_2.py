#!/usr/bin/python3
"""Change the name of a State object from the database using SQLAlchemy"""
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
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # id=2 olan state-i tapırıq
    state_to_update = session.query(State).get(2)
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()
