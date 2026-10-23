from models.proyecto import Proyecto
from models.proyecto_dao import ProyectoDAO
from views.proyecto_view import ProyectoView
from models.empleado_dao import EmpleadoDAO

class ProyectoController:
    def __init__(self):
        self.view = ProyectoView()

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
            elif opcion == 6:
                self.asignar_empleado()
            elif opcion == 7:
                self.quitar_empleado()
            elif opcion == 8:
                self.ver_empleados()
            elif opcion == 0:
                break
            else:
                self.view.mostrar_mensaje("Opción no válida")

    def agregar(self):
        try:
            datos = self.view.formulario_nuevo()
            if not datos["nombre"].strip():
                raise ValueError("Debe ingresar un nombre")
            obj = Proyecto(
                datos["nombre"],
                datos["descripcion"],
                datos["fecha_inicio"]
            )
            if ProyectoDAO.crear(obj):
                self.view.mostrar_mensaje("Agregado correctamente")
        except (ValueError, TypeError) as e:
            self.view.mostrar_mensaje(f"Error: {e}")

    def editar(self):
        obj = ProyectoDAO.obtener_por_id(self.view.solicitar_id())
        if not obj:
            self.view.mostrar_mensaje("No encontrado")
            return
        try:
            datos = self.view.formulario_editar(obj)
            if not datos["nombre"].strip():
                raise ValueError("Debe ingresar un nombre")
            obj.nombre = datos["nombre"]
            obj.descripcion = datos["descripcion"]
            obj.fecha_inicio = datos["fecha_inicio"]
            if ProyectoDAO.actualizar(obj):
                self.view.mostrar_mensaje("Actualizado correctamente")
        except (ValueError, TypeError) as e:
            self.view.mostrar_mensaje(f"Error: {e}")

    def eliminar(self):
        id_obj = self.view.solicitar_id()
        if self.view.confirmar_eliminacion():
            if ProyectoDAO.eliminar(id_obj):
                self.view.mostrar_mensaje("Eliminado correctamente")
            else:
                self.view.mostrar_mensaje("No se pudo eliminar")

    def imprimir_uno(self):
        obj = ProyectoDAO.obtener_por_id(self.view.solicitar_id())
        if obj:
            self.view.mostrar_objeto(obj)
        else:
            self.view.mostrar_mensaje("No encontrado")

    def imprimir_todos(self):
        self.view.mostrar_lista(ProyectoDAO.obtener_todos())
        
    def asignar_empleado(self):
        try:
            id_empleado = int(input("ID del empleado: "))
            id_proyecto = int(input("ID del proyecto: "))

            empleado = EmpleadoDAO.obtener_por_id(id_empleado)
            proyecto = ProyectoDAO.obtener_por_id(id_proyecto)

            if not empleado or not proyecto:
                self.view.mostrar_mensaje("Empleado o proyecto no encontrado")
                return

            if ProyectoDAO.asignar_empleado(id_empleado, id_proyecto):
                self.view.mostrar_mensaje("Empleado asignado correctamente")
            else:
                self.view.mostrar_mensaje("No se pudo asignar el empleado")

        except ValueError:
            self.view.mostrar_mensaje("Debe ingresar números válidos")
            
    def quitar_empleado(self):
        try:
            id_empleado = int(input("ID del empleado: "))
            id_proyecto = int(input("ID del proyecto: "))

            if ProyectoDAO.quitar_empleado(id_empleado, id_proyecto):
                self.view.mostrar_mensaje("Empleado quitado correctamente")
            else:
                self.view.mostrar_mensaje("No se encontró la asignación")

        except ValueError:
            self.view.mostrar_mensaje("Debe ingresar números válidos")

    def ver_empleados(self):
        id_proyecto = int(input("Ingrese el ID del proyecto: "))
        empleados = ProyectoDAO.ver_empleados(id_proyecto)

        if empleados:
            for empleado in empleados:
                print(f"ID: {empleado['id_empleado']} - Nombre: {empleado['nombre']}")
        else:
            self.view.mostrar_mensaje("No hay empleados asignados")