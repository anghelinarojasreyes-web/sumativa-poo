class Departamento:
    def __init__(self, nombre, gerente=None, id_departamento=None):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.gerente = gerente

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ValueError("Debe ingresar el nombre del departamento")
        self._nombre = valor

    def __str__(self):
        return f"Departamento [ID: {self.id_departamento}] | Nombre: {self.nombre} | Gerente: {self.gerente or 'Sin asignar'}"
