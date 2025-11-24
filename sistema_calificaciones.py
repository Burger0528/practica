"""while True:
    entrada=input("ingrese la calificacion ").strip().upper()
    if entrada == "FIN":
        print("gracias por usar el sistema")
        break
    try:
        calificacion= float(entrada)  
    except ValueError:
        print("ingrese un numero valido")
        continue
    if calificacion >4 and calificacion<=5:
        print("exelente")
    elif calificacion >3 and calificacion<=4:
        print("sobresaliente")
    elif calificacion> 2 and calificacion<= 3:
        print("aceptable")
    elif calificacion >1 and calificacion<= 2:
        print("reprobado")
    elif calificacion <= 1 and calificacion <0:
        print("deficiente")
    else:
        print("calificacion fuera de rango")
        
    """
"""ums=[1,2,3,4,50]
def ShowFirstAndLast(cosas):
    firts=cosas[0]
    last=cosas[4]
    return firts, last
valor1,valor2= ShowFirstAndLast(nums)

print(valor1)
print(valor2)"""



"""sumar = lambda num1, num2: num1 + num2
result = sumar(4,5)
print(result)"""
mylist=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre"]
print(mylist)
mylist.append("diciembre")
print(mylist)
print(mylist[0])
print(mylist[-1])
print(mylist.index("febrero"))
mylist.reverse()
print(mylist)
mylist.reverse()
print(mylist)
mylist.pop(3)
print(mylist)
mylist.sort()
print(mylist)