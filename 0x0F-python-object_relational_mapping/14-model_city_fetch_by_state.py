#!/usr/bin/python3
"""prints all City objects from the database"""
if __name__ == "__main__":
    from sys import argv
    from model_state import State
    from model_city import City
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, select
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    with Session(engine) as session:
        for city, state in session.query(City, State).join(State):
            print(f"{state.name}: ({city.id}) {city.name}")
