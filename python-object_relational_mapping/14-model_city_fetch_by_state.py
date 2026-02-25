#!/usr/bin/python3
"""List all City objects from the database hbtn_0e_14_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    # Session yaradılır
    Session = sessionmaker(bind=engine)
    session = Session()

    # Bütün şəhərləri id sırasına görə gətiririk
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        # State adını göstərmək üçün əlaqəli State obyektini tapırıq
        state = session.query(State).get(city.state_id)
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
