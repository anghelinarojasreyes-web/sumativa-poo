from models.empleado import Empleado
from models.empleado_dao import EmpleadoDAO
from models.departamento_dao import DepartamentoDAO
from views.empleado_view import EmpleadoView

class EmpleadoController:
    def __init__(self):
        self.view = EmpleadoView()

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
            departamento = DepartamentoDAO.obtener_por_id(datos["id_departamento"]) if datos["id_departamento"] else None

            if datos["id_departamento"] and departamento is None:
                self.view.mostrar_mensaje("El departamento no existe")
                return

            obj = Empleado(datos["nombre"], datos["correo"], datos["direccion"], datos["telefono"], datos["fecha_inicio"], datos["salario"], departamento)
            if EmpleadoDAO.crear(obj):
                self.view.mostrar_mensaje("Agregado correctamente")
        except (ValueError, TypeError) as e:
            self.view.mostrar_mensaje(f"Error: {e}")
            
    def editar(self):
        obj = EmpleadoDAO.obtener_por_id(self.view.solicitar_id())
        if not obj:
            self.view.mostrar_mensaje("No encontrado")
            return
        try:
            datos = self.view.formulario_editar(obj)
            departamento = DepartamentoDAO.obtener_por_id(datos["id_departamento"]) if datos["id_departamento"] else None

            if datos["id_departamento"] and departamento is None:
                self.view.mostrar_mensaje("El departamento no existe")
                return

            obj.nombre = datos["nombre"]
            obj.correo = datos["correo"]
            obj.direccion = datos["direccion"]
            obj.telefono = datos["telefono"]
            obj.fecha_inicio = datos["fecha_inicio"]
            obj.salario = datos["salario"]
            obj.departamento = departamento
            if EmpleadoDAO.actualizar(obj):
                self.view.mostrar_mensaje("Actualizado correctamente")
        except (ValueError, TypeError) as e:
            self.view.mostrar_mensaje(f"Error: {e}")

    def eliminar(self):
        id_obj = self.view.solicitar_id()
        if self.view.confirmar_eliminacion():
            if EmpleadoDAO.eliminar(id_obj):
                self.view.mostrar_mensaje("Eliminado correctamente")
            else:
                self.view.mostrar_mensaje("No se pudo eliminar")

    def imprimir_uno(self):
        obj = EmpleadoDAO.obtener_por_id(self.view.solicitar_id())
        if obj:
            self.view.mostrar_objeto(obj)
        else:
            self.view.mostrar_mensaje("No encontrado")

    def imprimir_todos(self):
        self.view.mostrar_lista(EmpleadoDAO.obtener_todos())
