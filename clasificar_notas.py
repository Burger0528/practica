def calasificar_notas():
    while True:
        try:
            nota = float(input(" ingrese una nota del 1 al 5 "))
            #nos aseguramos que la nota que ingrese este en ese rango
            if nota <1.0 or nota >5.0:
                print("la nota no esta en el rango esperado")
                continue
            break
            # se ejecuta el execpt si esciben algo que no sea un numero
        except ValueError:
            print("error, ingresa un valor numerico")
    
    if nota>3.0:
        print(" felicidades haz aprobado")
    else:
        print(" lo siento, has reprobado, sigue estudiando")
calasificar_notas()

