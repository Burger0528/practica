# productos.py
# Manejo del inventario: agregar, editar, eliminar y mostrar productos.

def mostrar_inventario(inventario):
    """Muestra todos los productos registrados."""
    if not inventario:
        print("No hay productos en el inventario.")
        return

    print("\n--- INVENTARIO ---")
    for producto in inventario:
        print(f"ID: {producto['id']} | Nombre: {producto['nombre']} | Marca: {producto['marca']} | "
              f"Categoría: {producto['categoria']} | Precio: {producto['precio']} | "
              f"Stock: {producto['stock']} | Garantía: {producto['garantia']} meses")
    print("-------------------")

def registrar_producto(inventario):
    """Agrega un nuevo producto al inventario con validación de campos vacíos."""
    print("\n--- REGISTRAR PRODUCTO ---")

    try:
        # Función interna para validar campos vacíos
        def pedir_campo(mensaje):
            valor = ""
            while not valor.strip():
                valor = input(mensaje).strip()
                if not valor:
                    print("⚠ Este campo no puede estar vacío.")
            return valor

        nuevo_id = len(inventario) + 1
        nombre = pedir_campo("Nombre del producto: ")
        marca = pedir_campo("Marca: ")
        categoria = pedir_campo("Categoría: ")

        # Valores numéricos con validación
        while True:
            try:
                precio = float(input("Precio unitario: "))
                break
            except ValueError:
                print("⚠ Ingrese un precio válido.")

        while True:
            try:
                stock = int(input("Cantidad en stock: "))
                break
            except ValueError:
                print("⚠ Ingrese una cantidad válida.")

        while True:
            try:
                garantia = int(input("Garantía (meses): "))
                break
            except ValueError:
                print("⚠ Ingrese un número válido.")

        inventario.append({
            "id": nuevo_id,
            "nombre": nombre,
            "marca": marca,
            "categoria": categoria,
            "precio": precio,
            "stock": stock,
            "garantia": garantia
        })

        print("Producto agregado correctamente.")

    except Exception:
        print("Ocurrió un error inesperado.")


def editar_producto(inventario):
    """Permite modificar un producto existente."""
    try:
        producto_id = int(input("\nID del producto a editar: "))
        producto = next((p for p in inventario if p["id"] == producto_id), None)

        if not producto:
            print("Producto no encontrado.")
            return

        print("Presione ENTER para dejar el valor actual.\n")

        nuevo_nombre = input(f"Nombre ({producto['nombre']}): ") or producto['nombre']
        nueva_marca = input(f"Marca ({producto['marca']}): ") or producto['marca']
        nueva_categoria = input(f"Categoría ({producto['categoria']}): ") or producto['categoria']

        nuevo_precio = input(f"Precio ({producto['precio']}): ")
        nuevo_precio = float(nuevo_precio) if nuevo_precio else producto['precio']

        nuevo_stock = input(f"Stock ({producto['stock']}): ")
        nuevo_stock = int(nuevo_stock) if nuevo_stock else producto['stock']

        nueva_garantia = input(f"Garantía meses ({producto['garantia']}): ")
        nueva_garantia = int(nueva_garantia) if nueva_garantia else producto['garantia']

        producto.update({
            "nombre": nuevo_nombre,
            "marca": nueva_marca,
            "categoria": nueva_categoria,
            "precio": nuevo_precio,
            "stock": nuevo_stock,
            "garantia": nueva_garantia
        })

        print("Producto actualizado correctamente.")

    except ValueError:
        print("Error: valores inválidos.")


def eliminar_producto(inventario):
    """Elimina un producto del inventario."""
    try:
        producto_id = int(input("\nID del producto a eliminar: "))
        producto = next((p for p in inventario if p["id"] == producto_id), None)

        if not producto:
            print("Producto no encontrado.")
            return

        inventario.remove(producto)
        print("Producto eliminado correctamente.")

    except ValueError:
        print("Error: ingrese un ID válido.")
