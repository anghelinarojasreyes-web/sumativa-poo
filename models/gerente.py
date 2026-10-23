from models.usuario import Usuario

class Gerente(Usuario):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo)
