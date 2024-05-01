from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String

from config.db import meta, engine

#meta.drop_all(engine)

users = Table("users", meta, Column(
    "id_user", Integer, primary_key=True),
      Column("name", String(255)),
      Column("email", String(255)))

meta.create_all(engine)
