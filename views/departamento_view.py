from views.utils import leer_numero, confirmar

class DepartamentoView:
    @staticmethod
    def mostrar_menu():
        print("\n--- GESTIÓN DE DEPARTAMENTOS ---")
        print("1.- Agregar departamento")
        print("2.- Editar departamento")
        print("3.- Eliminar departamento")
        print("4.- Imprimir un departamento")
        print("5.- Imprimir todos los departamentos")
        print("0.- Volver")
        return leer_numero("Seleccione una opción: ")

    @staticmethod
    def formulario_nuevo():
        nombre = input("Nombre: ")
        gerente = input("Gerente: ")
        return {"nombre": nombre, "gerente": gerente}

    @staticmethod
    def formulario_editar(obj):
        nombre = input(f"Nombre ({obj.nombre}): ") or obj.nombre
        gerente = input(f"Gerente ({obj.gerente}): ") or obj.gerente
        return {"nombre": nombre, "gerente": gerente}

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
