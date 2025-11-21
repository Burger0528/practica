#escribe un programa que graba del uno al 100, por cada multipo de 3 escribe fizz
# y por multiplo de 5 escribe buzz
# y si es de ambos escribe fizzbuzz



for i in range ( 0, 101):
    if i %3== 0 and i %5 == 0:
        print ("fizzbuzz")
    elif i %3 == 0:
        print("fizz")
    elif i %5== 0:
        print("buzz")
    else:
        print(i)