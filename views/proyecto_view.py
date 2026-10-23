from views.utils import leer_numero, confirmar

class ProyectoView:
    @staticmethod
    def mostrar_menu():
        print("\n--- GESTIÓN DE PROYECTOS ---")
        print("1.- Agregar proyecto")
        print("2.- Editar proyecto")
        print("3.- Eliminar proyecto")
        print("4.- Imprimir un proyecto")
        print("5.- Imprimir todos los proyectos")
        print("6.- Asignar empleado a proyecto")
        print("7.- Quitar empleado de proyecto")
        print("8.- Ver empleados asignados a un proyecto")
        print("0.- Volver")
        return leer_numero("Seleccione una opción: ")

    @staticmethod
    def formulario_nuevo():
        nombre = input("Nombre: ")
        descripcion = input("Descripción: ")
        fecha_inicio = input("Fecha de inicio: ")
        return {
            "nombre": nombre,
            "descripcion": descripcion,
            "fecha_inicio": fecha_inicio
        }

    @staticmethod
    def formulario_editar(obj):
        nombre = input(f"Nombre ({obj.nombre}): ") or obj.nombre
        descripcion = input(f"Descripción ({obj.descripcion}): ") or obj.descripcion
        fecha_inicio = input(f"Fecha de inicio ({obj.fecha_inicio}): ") or obj.fecha_inicio
        return {
            "nombre": nombre,
            "descripcion": descripcion,
            "fecha_inicio": fecha_inicio
        }

    @staticmethod
    def solicitar_id():
        return leer_numero("Ingrese el ID: ")

    @staticmethod
    def mostrar_objeto(obj):
        print(obj)

    @staticmethod
    def mostrar_lista(objetos):
        if not objetos:
            print("No hay registros")
        for obj in objetos:
            print(obj)

    @staticmethod
    def confirmar_eliminacion():
        return confirmar("¿Desea eliminarlo?")

    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)
