#!/usr/bin/python3
"""changes the name of a State object from the database"""
if __name__ == "__main__":
    from sys import argv
    from model_state import State
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, select
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    with Session(engine) as session:
        statement = select(State).where(State.id == 2)
        state = session.scalars(statement).first()
        state.name = "New Mexico"
        session.commit()
