import time  # para importar el time.sleep que hace que la consola tarde 1 segundo en imprimir 
try:
    numero_inicial= int(input("ingresa el numero para iniciar"))
    contador= numero_inicial
    print(f"iniciando cuenta regresiva desde {numero_inicial}")
    # el bucle es para ejecutar MIENTRAS el contador sea mayor que cero
    while contador> 0:
        print(contador)
        time.sleep(1)
        contador-= 1
except ValueError:
    print("ingrese un numero valido positivo")
except Exception as e:
    print("ocurrio un error")