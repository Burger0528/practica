#en este algorimo vamos a realizar un sistema de peluqueria de perritos, 
#solo para el registro de los peuditos 
peluditos = {}
#esta lista contendra  codigo unico, (, nombres, raza, peso)
def mostrar_menu():
    print("1. ver perritos registrados")
    print("2. registrar un peludito ")
    print("3. buscar un peludito")
    print("4. actualizar un peludito")
    print("5. eliminar un peludito")
    print("0. para salir ")

def mostrar_peluditos():
    if not peluditos:
        print("----------------------------")
        print("no hay peluditos registrados")
        print("----------------------------")
    else:
        for codigo_unico, (nombre, raza, peso) in peluditos.items():
            print(f"-codigo unico---   nombre---  raza---  peso")
            print(f"{codigo_unico}--- {nombre}---{raza}---{peso}")

def registrar_peludito():
    try:
        codigo=int(input("ingrese el codigo unico del perrito "))
        if codigo in peluditos:
            print("------------------------------ ")
            print("El peludito ya esta registrado ")
            print("------------------------------ ")
        else:
            while True:
                nombre = input("ingrese el nombre del peludito: ").strip()
                if nombre == "":
                    print(" el nombre no puede estar vacio")
                else:
                    break
            while True:
                raza = input("ingrese la raza del peludito: ").strip()
                if raza== "":
                    print(" la raza no puede quedar en vacio")
                else: 
                    break
            while True:
                try:
                    peso = float(input("ingrese el peso del peludito en kg: "))
                    break
                except ValueError:
                    print("ingrese un valor numerico en kg:")
            
            peluditos[codigo]=(nombre,raza,peso)
            print("------------------------------")
            print(f"{nombre}, fue registrado con exito")
            print(f"----------------------------------")

    except ValueError:
        print("ingrese un codigo numerico")

def buscar_un_peludito():
    try:
        codigo=int(input("ingrese el codigo unico del perrito "))
        if codigo in peluditos:
            nombre, raza, peso = peluditos[codigo]
            print(f" codigo,   nombre,  raza,  peso")
            print(f"{codigo}, {nombre}, {raza},{peso}")
        else:
            print("------------------------------")
            print("el codigo no existe en el sistema")
            print("---------------------------------")
    except ValueError:
        print("el codigo debe ser numerico ")

def actualizar_un_peludito():
    try:
        codigo=int(input("ingrese el codigo unico del perrito "))
        if codigo in peluditos:
            while True:
                nombre = input("ingrese el nombre del peludito: ").strip()
                if nombre == "":
                    print(" el nombre no puede estar vacio")
                else:
                    break
            while True:
                raza = input("ingrese la raza del peludito: ").strip()
                if raza== "":
                    print(" la raza no puede quedar en vacio")
                else: 
                    break
            while True:
                try:
                    peso = float(input("ingrese el peso del peludito en kg: "))
                    break
                except ValueError:
                    print("ingrese un valor numerico en kg:")
            
            peluditos[codigo],(nombre,raza,peso)
            print("------------------------------")
            print("peludito actualizado con exito")
            print("------------------------------")

        else:
            print("el codigo no exite en el sistema")
    except:
        print("ingrese un codigo valido ")

def eliminar_peludito():
    try:
        codigo=int(input("ingrese el codigo unico del perrito "))
        if codigo in peluditos:
            peluditos.pop(codigo)
            print("------------------------------")
            print(" peludito eliminado con exito ")
            print("------------------------------")


    except ValueError:
        print("ingrese un codigo numerico")
    

def main():
    while True:
        mostrar_menu()
        opcion= input("ingrese una opcion: ")
        if opcion == "1":
            mostrar_peluditos()
        elif opcion == "2":
            registrar_peludito()
        elif opcion == "3":
            buscar_un_peludito()
        elif opcion== "4":
            actualizar_un_peludito()
        elif  opcion == "5":
            eliminar_peludito()
        elif opcion == "0":
            break
        else: 
            print("ingrese una opcion numerica: ")            
if __name__ == "__main__":
    main()


