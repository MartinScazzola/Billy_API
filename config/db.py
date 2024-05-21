from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://dbname_86dq_user:v6iqY7V5Dku4ZzC8ROVejPtWUEZC0GTT@dpg-cool5le3e1ms73b7tj80-a.oregon-postgres.render.com/dbname_86dq"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

meta = MetaData()
conn = engine.connect()

#pass v6iqY7V5Dku4ZzC8ROVejPtWUEZC0GTT


