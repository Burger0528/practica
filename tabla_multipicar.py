#pedir el numero de la tabla que quiere multipicar
n=int(input("ingrese el numero de la tabnla que desea generar "))
print("________ la tabla de multiplicar {n}___________")
for i in range(1,11):
    resultado = n * i
    print(f"{n} x {i}= {resultado}")