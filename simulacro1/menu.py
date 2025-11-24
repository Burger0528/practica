# menu.py
# Módulo encargado del menú principal e interacción con el usuario.

from productos import (
    mostrar_inventario,
    registrar_producto,
    editar_producto,
    eliminar_producto
)

from ventas import (
    registrar_venta,
    mostrar_historial_ventas
)

from reportes import (
    generar_reportes
)

# IMPORTACIÓN DEL INVENTARIO Y VENTAS
from data import inventario, ventas


def mostrar_menu():
    """Muestra las opciones disponibles en el sistema."""
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Mostrar inventario")
    print("2. Registrar producto")
    print("3. Editar producto")
    print("4. Eliminar producto")
    print("5. Registrar venta")
    print("6. Ver historial de ventas")
    print("7. Reportes")
    print("8. Salir")


def ejecutar_menu():
    """Controla la ejecución del menú principal."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_inventario(inventario)

        elif opcion == "2":
            registrar_producto(inventario)

        elif opcion == "3":
            editar_producto(inventario)

        elif opcion == "4":
            eliminar_producto(inventario)

        elif opcion == "5":
            registrar_venta(inventario, ventas)

        elif opcion == "6":
            mostrar_historial_ventas(ventas)

        elif opcion == "7":
            generar_reportes(inventario, ventas)

        elif opcion == "8":
            print("Saliendo del sistema… ¡Hasta luego!")
            break

        else:
            print("Opción inválida, intente de nuevo.")


# ==========================
#      PUNTO DE ENTRADA
# ==========================

if __name__ == "__main__":
    ejecutar_menu()
