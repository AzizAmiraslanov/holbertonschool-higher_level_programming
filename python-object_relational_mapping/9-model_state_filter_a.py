#!/usr/bin/python3
"""List all State objects containing the letter 'a' using SQLAlchemy"""
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
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    # Session yaradılır
    Session = sessionmaker(bind=engine)
    session = Session()

    # 'a' hərfi olan state-ləri filterləyirik
    states_with_a = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .order_by(State.id)
        .all()
    )

    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    session.close()
