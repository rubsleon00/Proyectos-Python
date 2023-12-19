from random import *

palabras_secretas = ["abrigo","chaqueta","viento","lluvia","nayra","sueño"]
palabra_aleatoria = choice(palabras_secretas)
vidas = 6
letras_adivinadas = []


while vidas>0:
    palabra_buena = ""
    for letra in palabra_aleatoria:
        if letra in letras_adivinadas:
            palabra_buena += letra
        else:
            palabra_buena += "_"
    print(palabra_buena)

    if "_" not in palabra_buena:
        print("Ganaste")
        break

    letra_ingresada = input("Ingresa una letra: ")
    if letra_ingresada in letras_adivinadas:
        print("Letra repetida")
    elif letra_ingresada in palabra_aleatoria:
        print("Correcto")
        letras_adivinadas.append(letra_ingresada)
    else:
        print("Letra incorrecta")
        vidas-=1
        print(f"Te quedan {vidas} vidas")

    if vidas == 0:
        print(f"Perdiste, la palabra correcta era {palabra_aleatoria}")



