#!/usr/bin/python3
"""lists all State objects, and corresponding City objects"""
if __name__ == "__main__":
    from sys import argv
    from relationship_state import State
    from relationship_city import City
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, select
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    with Session(engine) as session:
        statement = select(State).order_by(State.id)
        states = session.scalars(statement)
        for state in states:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"    {city.id}: {city.name}")
