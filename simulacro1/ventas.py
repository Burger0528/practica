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


def registrar_venta(inventario, ventas):
    """Registra una venta y descuenta inventario."""
    try:
        print("\n--- REGISTRAR VENTA ---")

        # Cliente no vacío
        cliente = input("Nombre del cliente: ").strip()
        if not cliente:
            print("❌ El nombre del cliente no puede estar vacío.")
            return

        tipo_cliente = input("Tipo de cliente (Normal / VIP): ").strip().lower()
        if tipo_cliente not in ["normal", "vip"]:
            print("❌ Tipo de cliente inválido.")
            return

        # Validar ID numérico
        producto_id_str = input("ID del producto vendido: ").strip()
        if not producto_id_str.isdigit():
            print("❌ El ID debe ser un número.")
            return
        producto_id = int(producto_id_str)

        # Buscar producto
        producto = next((p for p in inventario if p["id"] == producto_id), None)
        if not producto:
            print("❌ Producto no encontrado.")
            return

        # Validar cantidad
        cantidad_str = input("Cantidad: ").strip()
        if not cantidad_str.isdigit():
            print("❌ La cantidad debe ser un entero.")
            return
        cantidad = int(cantidad_str)

        if cantidad <= 0:
            print("❌ La cantidad debe ser mayor a cero.")
            return

        if cantidad > producto["stock"]:
            print("❌ No hay suficiente stock.")
            return

        # Descuento
        descuento = 10 if tipo_cliente == "vip" else 0

        subtotal = producto["precio"] * cantidad
        total = subtotal - (subtotal * descuento / 100)

        # Actualizar stock
        producto["stock"] -= cantidad

        # Registrar venta
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        ventas.append({
            "cliente": cliente,
            "tipo_cliente": tipo_cliente,
            "producto": producto["nombre"],
            "marca": producto["marca"],
            "cantidad": cantidad,
            "precio_unitario": producto["precio"],
            "descuento": descuento,
            "total_pagado": total,
            "fecha": fecha
        })

        print("✅ Venta registrada exitosamente.")

    except Exception as e:
        print(f"⚠ Error inesperado: {e}")
