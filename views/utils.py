def leer_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingrese un número válido")

def confirmar(mensaje):
    return input(f"{mensaje} (si/no): ").lower() == "si"
