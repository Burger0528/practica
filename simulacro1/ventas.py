# ventas.py

from datetime import datetime

def mostrar_historial_ventas(ventas):
    """Muestra todas las ventas realizadas."""
    if not ventas:
        print("No hay ventas registradas.")
        return

    print("\n--- HISTORIAL DE VENTAS ---")
    for v in ventas:
        print(f"Cliente: {v['cliente']} | Producto: {v['producto']} | Cantidad: {v['cantidad']} | "
              f"Fecha: {v['fecha']} | Descuento: {v['descuento']}% | Total: ${v['total_pagado']}")
    print("---------------------------")


