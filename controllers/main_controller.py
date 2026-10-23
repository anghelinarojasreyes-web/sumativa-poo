from views.main_view import MainView
from controllers.empleado_controller import EmpleadoController
from controllers.departamento_controller import DepartamentoController
from controllers.proyecto_controller import ProyectoController
from controllers.registro_tiempo_controller import RegistroTiempoController

class MainController:
    def __init__(self):
        self.view = MainView()
        self.empleado_controller = EmpleadoController()
        self.departamento_controller = DepartamentoController()
        self.proyecto_controller = ProyectoController()
        self.registro_tiempo_controller = RegistroTiempoController()

    def ejecutar(self):
        while True:
            opcion = self.view.mostrar_menu()
            if opcion == 1:
                self.empleado_controller.ejecutar()
            elif opcion == 2:
                self.departamento_controller.ejecutar()
            elif opcion == 3:
                self.proyecto_controller.ejecutar()
            elif opcion == 4:
                self.registro_tiempo_controller.ejecutar()
            elif opcion == 0:
                print("Hasta luego")
                break
            else:
                print("Opción no válida")
