productos = {}
ventas = []
categorias = ("Móviles", "Computadoras", "Accesorios")
productos_en_oferta = set()


def agregar_producto(nombre, precio, stock):
    if nombre in productos:
        print("El producto ya existe.")
        return

    productos[nombre] = {"precio": precio, "stock": stock}
    print("Producto agregado correctamente.")


def eliminar_producto(nombre):
    if nombre in productos:
        del productos[nombre]
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")


def actualizar_precio(nombre, nuevo_precio):
    if nombre in productos:
        productos[nombre]["precio"] = nuevo_precio
        print("Precio actualizado.")
    else:
        print("Producto no encontrado.")


def registrar_venta(nombre, cantidad):
    if nombre not in productos:
        print("Producto no encontrado.")
        return

    if productos[nombre]["stock"] < cantidad:
        print("Stock insuficiente.")
        return

    productos[nombre]["stock"] -= cantidad
    total = productos[nombre]["precio"] * cantidad
    ventas.append(total)

    print(f"Venta registrada. Total: ${total:.2f}")


# Función recursiva
def suma_recursiva(lista):
    if not lista:
        return 0
    return lista[0] + suma_recursiva(lista[1:])
