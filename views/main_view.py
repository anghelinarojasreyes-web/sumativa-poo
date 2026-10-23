from views.utils import leer_numero

class MainView:
    @staticmethod
    def mostrar_menu():
        print("\n--- ECOTECH SOLUTIONS ---")
        print("1.- Gestión de Empleados")
        print("2.- Gestión de Departamentos")
        print("3.- Gestión de Proyectos")
        print("4.- Gestión de Registros de Tiempo")
        print("0.- Salir")
        return leer_numero("Seleccione una opción: ")
