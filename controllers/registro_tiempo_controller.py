from models.registro_tiempo import RegistroTiempo
from models.registro_tiempo_dao import RegistroTiempoDAO
from models.empleado_dao import EmpleadoDAO
from models.proyecto_dao import ProyectoDAO
from views.registro_tiempo_view import RegistroTiempoView

class RegistroTiempoController:
    def __init__(self):
        self.view = RegistroTiempoView()

    def ejecutar(self):
        while True:
            opcion = self.view.mostrar_menu()
            if opcion == 1:
                self.agregar()
            elif opcion == 2:
                self.editar()
            elif opcion == 3:
                self.eliminar()
            elif opcion == 4:
                self.imprimir_uno()
            elif opcion == 5:
                self.imprimir_todos()
            elif opcion == 0:
                break
            else:
                self.view.mostrar_mensaje("Opción no válida")

    def agregar(self):
        try:
            datos = self.view.formulario_nuevo()
            empleado = EmpleadoDAO.obtener_por_id(datos["id_empleado"])
            proyecto = ProyectoDAO.obtener_por_id(datos["id_proyecto"])

            if not empleado or not proyecto:
                self.view.mostrar_mensaje("Empleado o proyecto no encontrado")
                return

            if datos["horas"] <= 0:
                raise ValueError("Las horas deben ser mayores a cero")

            obj = RegistroTiempo(
                datos["fecha"],
                datos["horas"],
                datos["descripcion"],
                empleado,
                proyecto
            )
            if RegistroTiempoDAO.crear(obj):
                self.view.mostrar_mensaje("Agregado correctamente")
        except (ValueError, TypeError) as e:
            self.view.mostrar_mensaje(f"Error: {e}")

    def editar(self):
        obj = RegistroTiempoDAO.obtener_por_id(self.view.solicitar_id())
        if not obj:
            self.view.mostrar_mensaje("No encontrado")
            return
        try:
            datos = self.view.formulario_editar(obj)
            empleado = EmpleadoDAO.obtener_por_id(datos["id_empleado"])
            proyecto = ProyectoDAO.obtener_por_id(datos["id_proyecto"])

            if not empleado or not proyecto:
                self.view.mostrar_mensaje("Empleado o proyecto no encontrado")
                return

            if datos["horas"] <= 0:
                raise ValueError("Las horas deben ser mayores a cero")

            obj.fecha = datos["fecha"]
            obj.horas_trabajadas = datos["horas"]
            obj.descripcion = datos["descripcion"]
            obj.empleado = empleado
            obj.proyecto = proyecto

            if RegistroTiempoDAO.actualizar(obj):
                self.view.mostrar_mensaje("Actualizado correctamente")
        except (ValueError, TypeError) as e:
            self.view.mostrar_mensaje(f"Error: {e}")

    def eliminar(self):
        id_obj = self.view.solicitar_id()
        if self.view.confirmar_eliminacion():
            if RegistroTiempoDAO.eliminar(id_obj):
                self.view.mostrar_mensaje("Eliminado correctamente")
            else:
                self.view.mostrar_mensaje("No se pudo eliminar")

    def imprimir_uno(self):
        obj = RegistroTiempoDAO.obtener_por_id(self.view.solicitar_id())
        if obj:
            self.view.mostrar_objeto(obj)
        else:
            self.view.mostrar_mensaje("No encontrado")

    def imprimir_todos(self):
        self.view.mostrar_lista(RegistroTiempoDAO.obtener_todos())
