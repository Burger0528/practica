import random
limite_inferior = 1
limite_superior =20
numero_secreto= random.randint(limite_inferior,limite_superior) #  el programa por si solo escoge un numero al azar
adivinanza=0
intentos= 0
print("========================================")
print(f"¡Bienvenido al juego Adivina el Número!")
print(f"Estoy pensando en un número entre {limite_inferior} y {limite_superior}.")
print("========================================")
while adivinanza!= numero_secreto:
    try:
    #pedir adivinanza
        adivinanza=int(input("ingrese la adivinanza "))
        intentos +=1
        #dar pistas
        if adivinanza< numero_secreto:
            print("demasiado bajo")
        elif adivinanza> numero_secreto:
            print("demasiado alto")
    except ValueError:
            print("entrada no valida")
print("----------------------------------------")
print(f"🎉 ¡Felicidades! Adivinaste el número {numero_secreto}.")
print(f"Te tomó solo {intentos} intentos.")
print("----------------------------------------")
