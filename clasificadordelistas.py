# este es un clasificador de listas 
#creamos la lista original
lista=[0,2,4,5,-5,-6,7,0,9,0,-9,-20,10]
positivos=[]
negativos= []
ceros=[]
for i in lista:
    if i > 0:
        positivos.append(i)
    if i<0:
        negativos.append(i)
    if i == 0: 
        ceros.append(i)
print(lista)
print(ceros)
print(positivos)
print(negativos)