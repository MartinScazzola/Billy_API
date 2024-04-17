class InsertUserFailed(Exception):
    def __init__(self):
        super().__init__("Error al crear un usuario")

class DeleteUserFailed(Exception):
    def __init__(self):
        super().__init__("Error al borrar un usuario")