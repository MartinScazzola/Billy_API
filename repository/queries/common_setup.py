import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from repository.tables.users import Base

# We connect to the database using the ORM defined in tables.py
engine = create_engine(os.environ.get("DB_URI"))

# Create the tables in the database
Base.metadata.create_all(engine)

# Session is the handle of the database
Session = sessionmaker(bind=engine)
session = Session()
TIMEOUT = 60

session.close()