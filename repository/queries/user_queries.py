from repository.errors import DeleteUserFailed, InsertUserFailed
from repository.queries.common_setup import *
from repository.tables.users import User


def create_user(username, name, surname, password, email):
    try:
        new_user = User(username=username, name=name, surname=surname, password=password, email=email)
        
        session.add(new_user)
        
        session.commit()
        
        return new_user
    except Exception as e:
        session.rollback()
        raise InsertUserFailed()
    

def delete_user(user_id):
    try:
        user = session.query(User).filter_by(id=user_id).first()

        if user:
            session.delete(user)
            session.commit()
            return "Se elimino correctamente"
        else:
            raise DeleteUserFailed()
    except Exception as e:
        session.rollback()
        raise DeleteUserFailed()
