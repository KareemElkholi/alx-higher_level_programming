#!/usr/bin/python3
"""creates the State California with the City San Francisco"""
if __name__ == "__main__":
    from sys import argv
    from relationship_state import State, Base
    from relationship_city import City
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    with Session(engine) as session:
        Base.metadata.create_all(engine)
        state = State(name="California")
        city = City(name="San Francisco")
        state.cities.append(city)
        session.add(state)
        session.commit()
