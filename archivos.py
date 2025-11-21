while True:
    try:
        numero= int(input("ingrese un  numero del uno al 10 "))
        with open (f"tablas/tablas-{numero}.txt", "w") as archivo:
            
            for i in range (1,11):
                archivo.write (f"{numero} x {i}= {i * numero}\n")
        break
    except ValueError:
        print("ingrese un numeros")
            

#ejercicios
