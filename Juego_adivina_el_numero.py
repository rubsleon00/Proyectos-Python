from random import randint

intentos = 0
numero_secreto = randint(1,101)
nombre = (input("Cual es tu nombre: "))

print(f"Hola {nombre}, he pensado un número entre 1 y 100.\nTienes 8 intentos para adivinar cuál crees que es el número")

while intentos < 8:
    numero_estimado = int(input("Di un número: "))
    intentos += 1

    if numero_estimado < numero_secreto:
        print("El numero es mas alto")

    if numero_estimado > numero_secreto:
        print("El número es mas bajo")

    if numero_estimado == numero_secreto:
        print(f"El número es el correcto {nombre}¡ Lo has adivinado en {intentos} intentos")
        break

    if numero_estimado != numero_secreto:
        print(f"{nombre} no has adivinado el número. El número secreto era {numero_secreto}")










