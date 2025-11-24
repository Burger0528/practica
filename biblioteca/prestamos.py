# Módulo para registrar préstamos y devoluciones
from data import usuarios, libros, prestamos
from datetime import datetime

def registrar_prestamo():
    # Mostrar usuarios
    print("\n--- Usuarios ---")
    for u in usuarios:
        print(f"ID: {u['id']} | Nombre: {u['nombre']}")
    try:
        uid = int(input("ID del usuario que prestará un libro: "))
        usuario = next((u for u in usuarios if u["id"] == uid), None)
        if not usuario:
            print("Usuario no encontrado.")
            return

        # Verificar si ya tiene un libro prestado
        if any(p["usuario_id"] == uid and not p["devuelto"] for p in prestamos):
            print("❌ Este usuario ya tiene un libro prestado. Debe devolverlo antes.")
            return

        # Mostrar libros disponibles
        print("\n--- Libros disponibles ---")
        disponibles = [l for l in libros if l["disponible"]]
        if not disponibles:
            print("No hay libros disponibles.")
            return
        for l in disponibles:
            print(f"ID: {l['id']} | Título: {l['titulo']} | Autor: {l['autor']}")

        lid = int(input("ID del libro a prestar: "))
        libro = next((l for l in libros if l["id"] == lid), None)
        if not libro or not libro["disponible"]:
            print("Libro no disponible.")
            return

        # Registrar préstamo
        libro["disponible"] = False
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        prestamos.append({"usuario_id": uid, "libro_id": lid, "fecha_prestamo": fecha, "devuelto": False})
        print(f"✅ Préstamo registrado: {usuario['nombre']} -> {libro['titulo']}")

    except ValueError:
        print("⚠ ID inválido.")

def registrar_devolucion():
    print("\n--- Usuarios con libros prestados ---")
    prestados = [p for p in prestamos if not p["devuelto"]]
    if not prestados:
        print("No hay préstamos activos.")
        return
    for p in prestados:
        usuario = next(u for u in usuarios if u["id"] == p["usuario_id"])
        libro = next(l for l in libros if l["id"] == p["libro_id"])
        print(f"Usuario ID: {usuario['id']} | Libro ID: {libro['id']} | {libro['titulo']}")

    try:
        uid = int(input("ID del usuario que devuelve el libro: "))
        prestamo = next((p for p in prestamos if p["usuario_id"] == uid and not p["devuelto"]), None)
        if not prestamo:
            print("No hay préstamos activos para este usuario.")
            return
        libro = next(l for l in libros if l["id"] == prestamo["libro_id"])
        libro["disponible"] = True
        prestamo["devuelto"] = True
        print(f"✅ Libro {libro['titulo']} devuelto correctamente.")

    except ValueError:
        print("⚠ ID inválido.")
