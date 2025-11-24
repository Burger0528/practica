from usuarios import mostrar_usuarios, agregar_usuario, editar_usuario, eliminar_usuario
from libros import mostrar_libros, agregar_libro, editar_libro, eliminar_libro
from prestamos import registrar_prestamo, registrar_devolucion

def main_menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Agregar usuario")
        print("2. Mostrar usuarios")
        print("3. Editar usuario")
        print("4. Eliminar usuario")
        print("5. Agregar libro")
        print("6. Mostrar libros")
        print("7. Editar libro")
        print("8. Eliminar libro")
        print("9. Registrar préstamo")
        print("10. Registrar devolución")
        print("0. Salir")

        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            editar_usuario()
        elif opcion == "4":
            eliminar_usuario()
        elif opcion == "5":
            agregar_libro()
        elif opcion == "6":
            mostrar_libros()
        elif opcion == "7":
            editar_libro()
        elif opcion == "8":
            eliminar_libro()
        elif opcion == "9":
            registrar_prestamo()
        elif opcion == "10":
            registrar_devolucion()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    main_menu()
