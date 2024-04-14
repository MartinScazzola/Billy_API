# Billy_API

# Installs

* pip install SQLAlchemy alembic
* pip install psycopg2-binary

# ENVVAR
* export DB_URI=postgres://dbsecxhb:8Vo2eJAMmU8ydJnXGHzZlJpByc1Fw8SC@isabelle.db.elephantsql.com:5432/dbsecxhb


# Para generar el archivo de la migracion
- alembic -c repository/alembic.ini revision --autogenerate -m "mensaje que especifique los cambios de la migracion"

# Para ejecutar la migracion
- alembic -c repository/alembic.ini upgrade head


