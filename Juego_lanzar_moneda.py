from random import *

lista_numeros = [1,2,3,4,5,6]
caras = ["cara","cruz"]
aleatorio = choice(caras)



def lanzar_moneda():
    for moneda in aleatorio:
        return aleatorio

def probar_suerte(aleatorio,lista):
    if aleatorio == "cara":
        print("La lista se autodestruirá")
        return  []
    else:
        print("La lista fue salvada" )
        return lista

lanzar_moneda = probar_suerte(aleatorio,lista_numeros)
print(aleatorio,lanzar_moneda)








