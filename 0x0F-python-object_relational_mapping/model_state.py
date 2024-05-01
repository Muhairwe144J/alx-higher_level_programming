#!/usr/bin/python3
"""Defines the State class and creates the corresponding table in the database."""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an instance of Base
Base = declarative_base()

class State(Base):
    """Represents a state in the database."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the engine and bind it to the Base
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    print("Table 'states' created successfully!")
