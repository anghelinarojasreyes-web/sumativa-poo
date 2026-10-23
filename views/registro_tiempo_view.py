from views.utils import leer_numero, confirmar

class RegistroTiempoView:
    @staticmethod
    def mostrar_menu():
        print("\n--- REGISTROS DE TIEMPO ---")
        print("1.- Agregar registro")
        print("2.- Editar registro")
        print("3.- Eliminar registro")
        print("4.- Imprimir un registro")
        print("5.- Imprimir todos los registros")
        print("0.- Volver")
        return leer_numero("Seleccione una opción: ")

    @staticmethod
    def leer_horas(mensaje):
        while True:
            try:
                horas = float(input(mensaje))
                if horas <= 0:
                    print("Las horas deben ser mayores a cero")
                else:
                    return horas
            except ValueError:
                print("Ingrese un número válido")

    @staticmethod
    def formulario_nuevo():
        fecha = input("Fecha: ")
        horas = RegistroTiempoView.leer_horas("Horas trabajadas: ")
        descripcion = input("Descripción: ")
        id_empleado = leer_numero("ID del empleado: ")
        id_proyecto = leer_numero("ID del proyecto: ")
        return {
            "fecha": fecha,
            "horas": horas,
            "descripcion": descripcion,
            "id_empleado": id_empleado,
            "id_proyecto": id_proyecto
        }

    @staticmethod
    def formulario_editar(obj):
        fecha = input(f"Fecha ({obj.fecha}): ") or obj.fecha
        horas_texto = input(f"Horas ({obj.horas_trabajadas}): ")
        if horas_texto:
            while True:
                try:
                    horas = float(horas_texto)
                    if horas > 0:
                        break
                    else:
                        print("Las horas deben ser mayores a cero")
                except ValueError:
                    print("Ingrese un número válido")
                horas_texto = input("Horas trabajadas: ")
        else:
            horas = obj.horas_trabajadas
        descripcion = input(f"Descripción ({obj.descripcion}): ") or obj.descripcion
        id_empleado = leer_numero("ID del empleado: ")
        id_proyecto = leer_numero("ID del proyecto: ")
        return {
            "fecha": fecha,
            "horas": horas,
            "descripcion": descripcion,
            "id_empleado": id_empleado,
            "id_proyecto": id_proyecto
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
