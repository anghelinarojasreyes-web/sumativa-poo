from views.utils import leer_numero, confirmar

class EmpleadoView:
    @staticmethod
    def mostrar_menu():
        print("\n--- GESTIÓN DE EMPLEADOS ---")
        print("1.- Agregar empleado")
        print("2.- Editar empleado")
        print("3.- Eliminar empleado")
        print("4.- Imprimir un empleado")
        print("5.- Imprimir todos los empleados")
        print("0.- Volver")
        return leer_numero("Seleccione una opción: ")

    @staticmethod
    def formulario_nuevo():
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        fecha_inicio = input("Fecha de inicio: ")
        salario = float(input("Salario: "))
        id_depto = leer_numero("ID departamento (0 si no tiene): ")
        return {"nombre": nombre, "correo": correo, "direccion": direccion, "telefono": telefono, "fecha_inicio": fecha_inicio, "salario": salario, "id_departamento": id_depto}

    @staticmethod
    def formulario_editar(obj):
        nombre = input(f"Nombre ({obj.nombre}): ") or obj.nombre
        correo = input(f"Correo ({obj.correo}): ") or obj.correo
        direccion = input(f"Dirección ({obj.direccion}): ") or obj.direccion
        telefono = input(f"Teléfono ({obj.telefono}): ") or obj.telefono
        fecha_inicio = input(f"Fecha de inicio ({obj.fecha_inicio}): ") or obj.fecha_inicio
        salario_texto = input(f"Salario ({obj.salario}): ")
        salario = float(salario_texto) if salario_texto else obj.salario
        id_actual = obj.departamento.id_departamento if obj.departamento else 0
        id_texto = input(f"ID departamento ({id_actual}): ")
        id_departamento = int(id_texto) if id_texto else id_actual
        return {"nombre": nombre, "correo": correo, "direccion": direccion, "telefono": telefono, "fecha_inicio": fecha_inicio, "salario": salario, "id_departamento": id_departamento}

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
