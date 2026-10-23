class RegistroTiempo:
    def __init__(self, fecha, horas_trabajadas, descripcion, empleado, proyecto, id_registro=None):
        self.id_registro = id_registro
        self.fecha = fecha
        self.horas_trabajadas = horas_trabajadas
        self.descripcion = descripcion
        self.empleado = empleado
        self.proyecto = proyecto

    def __str__(self):
        return f"Registro [ID: {self.id_registro}] | Fecha: {self.fecha} | Horas: {self.horas_trabajadas} | Descripción: {self.descripcion} | Empleado: {self.empleado.nombre} | Proyecto: {self.proyecto.nombre}"