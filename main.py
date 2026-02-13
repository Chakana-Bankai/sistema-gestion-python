from data_manager import (
    agregar_producto,
    eliminar_producto,
    actualizar_precio,
    registrar_venta,
    productos,
    ventas
)

from reports import (
    mostrar_productos,
    calcular_total_ventas,
    exportar_productos_csv,
    exportar_ventas_txt
)

from validations import validar_float, validar_int


def menu():
    while True:
        print("\n===== SISTEMA DE GESTIÓN =====")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Actualizar precio")
        print("4. Eliminar producto")
        print("5. Registrar venta")
        print("6. Total ventas")
        print("7. Exportar datos")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = validar_float(input("Precio: "))
            stock = validar_int(input("Stock: "))

            if precio is not None and stock is not None:
                agregar_producto(nombre, precio, stock)

        elif opcion == "2":
            mostrar_productos()

        elif opcion == "3":
            nombre = input("Producto a actualizar: ")
            nuevo_precio = validar_float(input("Nuevo precio: "))
            if nuevo_precio is not None:
                actualizar_precio(nombre, nuevo_precio)

        elif opcion == "4":
            nombre = input("Producto a eliminar: ")
            eliminar_producto(nombre)

        elif opcion == "5":
            nombre = input("Producto vendido: ")
            cantidad = validar_int(input("Cantidad: "))
            if cantidad is not None:
                registrar_venta(nombre, cantidad)

        elif opcion == "6":
            total = calcular_total_ventas()
            print(f"Total acumulado en ventas: ${total:.2f}")

        elif opcion == "7":
            exportar_productos_csv(productos)
            exportar_ventas_txt(ventas)

        elif opcion == "8":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
