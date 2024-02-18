#!/usr/bin/python3
"""lists all State objects that contain the letter a from the database"""
if __name__ == "__main__":
    from sys import argv
    from model_state import State
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, select
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    with Session(engine) as session:
        statement = select(State).filter(State.name.contains("a"))
        for state in session.scalars(statement):
            session.delete(state)
        session.commit()
