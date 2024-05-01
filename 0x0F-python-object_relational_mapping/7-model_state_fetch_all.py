#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the engine and bind it to the Base
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db_name),
                           pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and sort by id
    states = session.query(State).order_by(State.id).all()

    # Display the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
