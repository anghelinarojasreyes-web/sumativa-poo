from models.usuario import Usuario

class Empleado(Usuario):
    def __init__(self, nombre, correo, direccion, telefono, fecha_inicio, salario, departamento=None, id_empleado=None):
        super().__init__(nombre, correo)
        self.id_empleado = id_empleado
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_inicio = fecha_inicio
        self.salario = salario
        self.departamento = departamento

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor < 0:
            raise ValueError("El salario no puede ser negativo")
        self._salario = valor

    def __str__(self):
        departamento = self.departamento.nombre if self.departamento else "Sin departamento"
        return f"Empleado [ID: {self.id_empleado}] | {self.nombre} | {self.correo} | {self.direccion} | {self.telefono} | {self.fecha_inicio} | ${self.salario} | {departamento}"
