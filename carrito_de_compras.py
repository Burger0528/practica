productos = {
    1: ("Manzana", 0.5),
    2: ("Pan", 1.0),
    3: ("Leche", 1.5),
    4: ("Queso", 2.5)
}
claves = list(productos.keys())
print(claves)
carrito={}


def mostrar_menu():
    print("menu principal")
    print("1. ver productos")
    print("2. agregar productos al carrito")
    print("3. ver carrito")
    print("4. eliminar productos")
    print("5. finalizar compras")
    print("0. salir")

def mostrar_productos(productos):
    print("======== PRODUCTOS DISPONIBLES=======")
    for codigo,(nombre, precio) in productos.items():
        print(f"{codigo} . {nombre}- ${precio:.2f}")

def mostrar_carrito():
    if not carrito:
        print("El carrito esta vacio")
    else:
        print("======= CARRITO DE COMPRAS======")
        total = 0
        for codigo, cantidad in carrito.items():
            nombre, precio = productos[codigo]
            subtotal = precio * cantidad
            total += subtotal
            print(f"{nombre} x {cantidad}-${subtotal}")
            print(f" TOTAL ${total}")

def agregar_producto():
        mostrar_productos(productos)
        try:    
            codigo=int(input("Ingrese el codigo del producto"))
            if codigo in productos:
                cantidad = int(input("Ingrese la candtidad "))
                carrito[codigo] = carrito.get(codigo, 0 ) + cantidad
                print(f" se agregraon {cantidad}  {productos[codigo][0]} al carrito")
            else:
                print("codigo invalido")
        except ValueError:
            print("entrada invalida, intente de nuevo")

def eliminar_producto():
    if not carrito:
        print ("el carrito esta vacio")
        return            
    mostrar_carrito()
    try: 
        codigo= int(input(" ingrese el codigo del producto a eliminar "))
        if codigo in carrito:
            del carrito[codigo]
            print("eliminado correctamente")
        else:
            print("el producto no s eencuentra en el carrito")
    except ValueError:
        print(" entrada no valida")

def finalizar_compra():
    mostrar_carrito()
    if carrito :
        print( "gracvias por su compra ")
        carrito.clear()
    else: 
        print(" no hay productos en el carrito")    

while True:
    mostrar_menu()
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        mostrar_productos(productos)
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        mostrar_carrito()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        finalizar_compra()
    elif opcion == "0":
        print("\n¡Hasta luego!")
        break
    else:
        print("❌ Opción no válida. Intente de nuevo.")