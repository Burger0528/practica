frutas=["naranja","pera","manzana"]
print(frutas)
frutas.append("banana")
print(frutas)

#frutas.remove("naranja")
print(frutas)


frutas.insert(1,"tomate")
print(frutas)

frutas.pop(-1)
print(frutas)

esta_banana= "pera" in frutas
print(esta_banana)
esta_banana=frutas.index("pera")
print(esta_banana)




for i in range(0,101,8):
    print(f"hoala mundo {1}")