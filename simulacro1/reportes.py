# reportes.py
# Módulo encargado de generar todos los reportes del sistema.

def top_productos_mas_vendidos(ventas):
    """Retorna los 3 productos más vendidos según cantidad total."""
    conteo = {}

    for venta in ventas:
        nombre = venta["producto"]
        conteo[nombre] = conteo.get(nombre, 0) + venta["cantidad"]

    # Ordenar de mayor a menor y devolver top 3
    return sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:3]


def ventas_por_marca(ventas):
    """Agrupa ventas por marca y suma cantidades vendidas."""
    agrupado = {}

    for venta in ventas:
        marca = venta["marca"]
        agrupado[marca] = agrupado.get(marca, 0) + venta["cantidad"]

    return agrupado


def calcular_ingresos(ventas):
    """Calcula ingreso bruto y neto (descuento aplicado)."""
    ingreso_bruto = sum(v["cantidad"] * v["precio_unitario"] for v in ventas)
    ingreso_neto = sum(v["total_pagado"] for v in ventas)
    return ingreso_bruto, ingreso_neto


def rendimiento_inventario(inventario, ventas):
    """Retorna cuánto se vendió vs cuánto había en inventario."""
    resultado = []

    for producto in inventario:
        vendido = sum(v["cantidad"] for v in ventas if v["producto"] == producto["nombre"])
        total_inicial = producto["stock"] + vendido  # stock original

        porcentaje = (vendido / total_inicial * 100) if total_inicial > 0 else 0

        resultado.append({
            "producto": producto["nombre"],
            "vendido": vendido,
            "inventario_inicial": total_inicial,
            "rendimiento": round(porcentaje, 2)
        })

    return resultado


def generar_reportes(inventario, ventas):
    """Imprime los reportes completos en pantalla."""
    print("\n=== REPORTES DEL SISTEMA ===")

    # Top 3 productos
    top = top_productos_mas_vendidos(ventas)
    print("\n--- Top 3 productos más vendidos ---")
    if top:
        for nombre, cantidad in top:
            print(f"{nombre}: {cantidad} unidades")
    else:
        print("No hay ventas registradas.")

    # Ventas agrupadas por marca
    print("\n--- Ventas agrupadas por marca ---")
    marcas = ventas_por_marca(ventas)
    if marcas:
        for marca, cantidad in marcas.items():
            print(f"{marca}: {cantidad} unidades")
    else:
        print("No hay ventas registradas.")

    # Ingresos
    print("\n--- Ingresos ---")
    bruto, neto = calcular_ingresos(ventas)
    print(f"Ingreso bruto: ${bruto}")
    print(f"Ingreso neto:  ${neto}")

    # Rendimiento del inventario
    print("\n--- Rendimiento del inventario ---")
    rend = rendimiento_inventario(inventario, ventas)
    for r in rend:
        print(f"{r['producto']} | Vendido: {r['vendido']} | Inventario inicial: {r['inventario_inicial']} | "
              f"Rendimiento: {r['rendimiento']}%")

    print("\n==============================")
