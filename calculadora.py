try:
    number1= float(input("ingresa un numero entero"))
except ValueError:
    print("invalido, ingrese un numero valido")
    number1=0.0         
try:
    number2=float(input("ingrese un segundo numero entero"))
except ValueError:
    print("invalido, ingrese un numero valido")
    number2=0.0
#solicito una operacion
operacion=input("ingrese una operacion (+, -, *, /)")
#inicializo una variable para el resultado
resultado = 0
if operacion == '+':
    resultado=(number1 + number2)
elif operacion== '-':
    resultado= (number1 -  number2)
elif operacion== '*':
    resultado= (number1 *  number2)
elif operacion== '/':
    if number2!= 0:
        resultado= (number1 /  number2)
    else:
        print("no se puede dividir por cero")
if operacion in 8('+', '-', '*', '/') and not (operacion =='/' and number2==0):
    print(f"{number1} {operacion} {number2}  = {resultado}")
else:
    print("hubo un error en el calculo5")

