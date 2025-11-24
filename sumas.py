sumatoria= 0
contador= -1
while contador !=0:
    try:
        entrada = int(input("ingrese los numeros para ir sumando"))
        contador= entrada
        if contador!=0:
            sumatoria+=entrada
            print(f"la suma va en {sumatoria}")
        else:
            print("el programa finalizo")
            break

    except ValueError:
        print("ingrese un numero valido")
