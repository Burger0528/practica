numeros_pares=[]
with open ( "tablas/tabla_numerosa_pares.txt", "w") as file:
   for i in range( 1,100):
        if i% 2==0:
        result = numeros_pares.append(i)
        file.write(f"la lista de numeros pares es{result}\n") 
