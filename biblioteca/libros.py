# Módulo para manejar libros de la biblioteca
from data import libros

def mostrar_libros():
    if not libros:
        print("No hay libros registrados.")
        return
    print("\n--- LIBROS ---")
    for l in libros:
        estado = "Disponible" if l["disponible"] else "Prestado"
        print(f"ID: {l['id']} | Título: {l['titulo']} | Autor: {l['autor']} | Estado: {estado}")
    print("----------------")

def agregar_libro():
    titulo = input("Título del libro: ").strip()
    autor = input("Autor: ").strip()
    if not titulo or not autor:
        print("⚠ Los campos no pueden estar vacíos.")
        return
    nuevo_id = len(libros) + 1
    libros.append({"id": nuevo_id, "titulo": titulo, "autor": autor, "disponible": True})
    print(f"✅ Libro {titulo} agregado.")

def editar_libro():
    mostrar_libros()
    try:
        lid = int(input("ID del libro a editar: "))
        libro = next((l for l in libros if l["id"] == lid), None)
        if not libro:
            print("Libro no encontrado.")
            return
        nuevo_titulo = input(f"Título ({libro['titulo']}): ").strip() or libro["titulo"]
        nuevo_autor = input(f"Autor ({libro['autor']}): ").strip() or libro["autor"]
        libro["titulo"] = nuevo_titulo
        libro["autor"] = nuevo_autor
        print("✅ Libro actualizado.")
    except ValueError:
        print("⚠ ID inválido.")

def eliminar_libro():
    mostrar_libros()
    try:
        lid = int(input("ID del libro a eliminar: "))
        libro = next((l for l in libros if l["id"] == lid), None)
        if not libro:
            print("Libro no encontrado.")
            return
        libros.remove(libro)
        print("✅ Libro eliminado.")
    except ValueError:
        print("⚠ ID inválido.")
