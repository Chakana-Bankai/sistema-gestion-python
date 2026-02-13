import csv
from data_manager import suma_recursiva


def mostrar_productos():
    from data_manager import productos

    if not productos:
        print("No hay productos registrados.")
        return

    for nombre, datos in productos.items():
        print(
            f"{nombre} | Precio: ${datos['precio']} | Stock: {datos['stock']}"
        )


def calcular_total_ventas():
    from data_manager import ventas
    return suma_recursiva(ventas)


def exportar_productos_csv(productos):
    with open("data/productos.csv", "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Producto", "Precio", "Stock"])

        for nombre, datos in productos.items():
            writer.writerow([nombre, datos["precio"], datos["stock"]])

    print("Productos exportados a productos.csv")


def exportar_ventas_txt(ventas):
    with open("data/ventas.txt", "w") as archivo:
        for venta in ventas:
            archivo.write(f"{venta}\n")

    print("Ventas exportadas a ventas.txt")
