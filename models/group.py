from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String

from config.db import meta, engine

#meta.drop_all(engine)

groups = Table("groups", meta, Column(
    "id_group", Integer, primary_key=True),
      Column("name", String(255)),)


group_participants = Table("participants", meta, 
                           Column('id_user', Integer, ForeignKey('users.id_user', ondelete='CASCADE'), primary_key=True, nullable=False),
                           Column('id_group', Integer, ForeignKey('groups.id_group', ondelete='CASCADE'), primary_key=True, nullable=False))

group_expenses = Table("group_expenses", meta, Column("id_expense", Integer, primary_key=True),
                           Column('id_group', Integer, ForeignKey('groups.id_group', ondelete='CASCADE'), nullable=False),
                           Column('id_user', Integer, ForeignKey('users.id_user', ondelete='CASCADE'), nullable=False),
                           Column('amount', Integer),
                           Column('currency', String(255)),
                           Column('name', String(255)))


expense_participants = Table("expense_participants", meta, 
                           Column('id_expense', Integer, ForeignKey('group_expenses.id_expense', ondelete='CASCADE'), primary_key=True, nullable=False),
                           Column('id_user', Integer, ForeignKey('users.id_user', ondelete='CASCADE'), primary_key=True, nullable=False),
                           Column('amount', Integer))


meta.create_all(engine)
