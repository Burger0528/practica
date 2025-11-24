"""
numbers= [10,15,12,11,12,14,1,2,23,25,24,26,28]

#creo una lista de solo incluye los numeros pares
pares=[num for num in numbers if num%2==0]
print(numbers)
print(pares)
"""

numbers= [10,15,12,11,12,14,1,2,23,25,24,26,28]
lista_pares = []
for i in numbers:
    if i% 2 ==0:
        if i not in numbers:
            lista_pares.append(i)
            
print(numbers)
print(lista_pares)