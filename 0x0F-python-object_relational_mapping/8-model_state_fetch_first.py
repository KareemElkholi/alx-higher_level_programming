#!/usr/bin/python3
"""prints the first State object from the database"""
if __name__ == "__main__":
    from sys import argv
    from model_state import State
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, select
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    with Session(engine) as session:
        statement = select(State).order_by(State.id)
        state = session.scalars(statement).first()
        if state:
            print(f"{state.id}: {state.name}")
        else:
            print("Nothing")
