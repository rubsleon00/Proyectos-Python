def numero_perfumeria():
    for n in range(1,10000):
        yield f"P - {n}"

def numero_farmacia():
    for n in range(1,10000):
        yield f"F - {n}"

def numero_cosmetica():
    for n in range(1,10000):
        yield f"C - {n}"

p = numero_perfumeria()
f = numero_farmacia()
c = numero_cosmetica()

def decorador(rubro):
    print("\n" + "*" * 23)
    print("Su numero es: ")
    if rubro == "P":
        print(next(p))
    elif rubro == "F":
        print(next(f))
    else:
        print(next(c))

    print("Aguarde y seá atendido")
    print("*" * 23 + "\n")