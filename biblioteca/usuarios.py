# Módulo para manejar usuarios de la biblioteca
from data import usuarios

def mostrar_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    print("\n--- USUARIOS ---")
    for u in usuarios:
        print(f"ID: {u['id']} | Nombre: {u['nombre']}")
    print("----------------")

def agregar_usuario():
    nombre = input("Nombre del usuario: ").strip()
    if not nombre:
        print("⚠ El nombre no puede estar vacío.")
        return
    nuevo_id = len(usuarios) + 1
    usuarios.append({"id": nuevo_id, "nombre": nombre})
    print(f"✅ Usuario {nombre} agregado correctamente.")

def editar_usuario():
    mostrar_usuarios()
    try:
        uid = int(input("ID del usuario a editar: "))
        usuario = next((u for u in usuarios if u["id"] == uid), None)
        if not usuario:
            print("Usuario no encontrado.")
            return
        nuevo_nombre = input(f"Nombre ({usuario['nombre']}): ").strip() or usuario["nombre"]
        usuario["nombre"] = nuevo_nombre
        print("✅ Usuario actualizado.")
    except ValueError:
        print("⚠ ID inválido.")

def eliminar_usuario():
    mostrar_usuarios()
    try:
        uid = int(input("ID del usuario a eliminar: "))
        usuario = next((u for u in usuarios if u["id"] == uid), None)
        if not usuario:
            print("Usuario no encontrado.")
            return
        usuarios.remove(usuario)
        print("✅ Usuario eliminado.")
    except ValueError:
        print("⚠ ID inválido.")
