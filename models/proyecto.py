class Proyecto:
    def __init__(self, nombre, descripcion, fecha_inicio, id_proyecto=None):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio

    def __str__(self):
        return f"Proyecto [ID: {self.id_proyecto}] | {self.nombre} | {self.descripcion} | {self.fecha_inicio}"
