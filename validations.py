def validar_float(valor):
    try:
        return float(valor)
    except ValueError:
        print("Debe ingresar un número válido.")
        return None


def validar_int(valor):
    try:
        return int(valor)
    except ValueError:
        print("Debe ingresar un número entero válido.")
        return None
