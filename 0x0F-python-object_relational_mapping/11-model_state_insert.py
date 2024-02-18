#!/usr/bin/python3
"""adds the State object “Louisiana” to the database"""
if __name__ == "__main__":
    from sys import argv
    from model_state import State
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, select
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    with Session(engine) as session:
        session.add(State(name="Louisiana"))
        session.commit()
        statement = select(State).filter(State.name == "Louisiana")
        state = session.scalars(statement).first()
        print(state.id)
