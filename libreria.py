libros={}
#codigo - nombre, cantidad, precio
def mostar_menu():
    print("----menu----")
    print("1. ver libros")
    print("2. agregar libros")
    print("3. buscar libros")
    print("4. eliminar libro")
    print("5. actualizar libro")
    print("6. salir")

def ver_libros():
    if not libros:
        print("no hay libros para mostrar")
        print("--------")
        
    else:
        for codigo, (nombre, cantidad, valor) in libros.items():
            
            print(" --codigo----- libro------cantidad--- -valor")
            print(f" {codigo}--- {nombre}---{cantidad}-- ${valor}")

def aregregar_libros():
    try: 
        codigo = int(input("agregue el codigo del libro"))
        if codigo in libros:
            print("el libro ya existe ")
            return
        nombre= input("agregue el nombre del libro")
        cantidad= input("agregue la cantidad de libros ")
        valor= float(input("agregue el valor"))
        libros[codigo]= nombre, cantidad, valor
        print("libro registrado con exito")        
    except ValueError:
        print("ingrese un codigo valido")

def actualizar_libros():
    try:
        codigo= int(input("ingrese el codigo del libro a actualizar"))
        if codigo in libros:
            nombre= input("agregue el nombre del libro")
            cantidad= input("agregue la cantidad de libros ")
            valor= float(input("agregue el valor"))
            libros[codigo]= nombre, cantidad, valor
            print("libro actualizado con exito")
        else: 
            print("el codigo no exite ")
    except ValueError:
        print("Agregue un codigo valido")

def eliminar_libros():
    try:
        codigo= int(input("ingrese el codigo del libro a eliminar"))
        if codigo in libros:
           eliminado = libros.pop(codigo)
           print("eliminado con exito")
        else:
            print("El libro no existe")
    except ValueError:
        print("ingrese un codigo valido")

def buscar_producto():
    try:
        codigo= int(input("ingrese el codigo del libro a buscar"))
        if codigo in libros:
            nombre, cantidad,valor = libros[codigo]
            print("PRODUCTO ENCONTRADO")
            print(f"{codigo}--{nombre}---{cantidad}---{valor}")
        else:
            print("codigo no encontrado")

    except ValueError:
        print("ingrese un numero valido ")

def menu():
   
    while True: 
        mostar_menu()
        opcion = input("ingrese una opcion ")
        if opcion == "1":
            ver_libros()
        elif opcion == "2":
            aregregar_libros()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            eliminar_libros()

if __name__ == "__main__":
    menu()






