from models.departamento import Departamento
from models.departamento_dao import DepartamentoDAO
from views.departamento_view import DepartamentoView

class DepartamentoController:
    def __init__(self):
        self.view = DepartamentoView()

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
            obj = Departamento(datos["nombre"], datos["gerente"])
            if DepartamentoDAO.crear(obj):
                self.view.mostrar_mensaje("Agregado correctamente")
        except (ValueError, TypeError) as e:
            self.view.mostrar_mensaje(f"Error: {e}")

    def editar(self):
        obj = DepartamentoDAO.obtener_por_id(self.view.solicitar_id())
        if not obj:
            self.view.mostrar_mensaje("No encontrado")
            return
        try:
            datos = self.view.formulario_editar(obj)
            obj.nombre = datos["nombre"]
            obj.gerente = datos["gerente"]
            if DepartamentoDAO.actualizar(obj):
                self.view.mostrar_mensaje("Actualizado correctamente")
        except (ValueError, TypeError) as e:
            self.view.mostrar_mensaje(f"Error: {e}")

    def eliminar(self):
        id_obj = self.view.solicitar_id()
        if self.view.confirmar_eliminacion():
            if DepartamentoDAO.eliminar(id_obj):
                self.view.mostrar_mensaje("Eliminado correctamente")
            else:
                self.view.mostrar_mensaje("No se pudo eliminar")

    def imprimir_uno(self):
        obj = DepartamentoDAO.obtener_por_id(self.view.solicitar_id())
        if obj:
            self.view.mostrar_objeto(obj)
        else:
            self.view.mostrar_mensaje("No encontrado")

    def imprimir_todos(self):
        self.view.mostrar_lista(DepartamentoDAO.obtener_todos())
