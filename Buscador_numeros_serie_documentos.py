import os
import re
from datetime import datetime
import time
import math


def buscar_numeros_serie(directorio_raiz):
    fecha_actual = datetime.now().strftime("%d/%m/%y")
    numeros_encontrados = []
    duracion_busqueda = 0

    tiempo_inicio = time.time()

    # Recorrer el árbol de carpetas
    for directorio_actual, carpetas, archivos in os.walk(directorio_raiz):
        for archivo in archivos:
            ruta_archivo = os.path.join(directorio_actual, archivo)

            # Leer el contenido del archivo
            with open(ruta_archivo, 'r') as file:
                contenido = file.read()

            # Buscar el número de serie en el contenido del archivo
            resultado_busqueda = re.search(r'\b[N]\w{3}-\d{5}\b', contenido)

            if resultado_busqueda:
                numero_serie = resultado_busqueda.group()
                numeros_encontrados.append((archivo, numero_serie))

    tiempo_fin = time.time()
    duracion_busqueda = math.ceil(tiempo_fin - tiempo_inicio)

    # Mostrar los resultados
    print("-" * 50)
    print("Fecha de búsqueda:", fecha_actual)
    print("\nARCHIVO\t\t\t\tNRO. SERIE")
    print("-------\t\t\t\t----------")
    for archivo, numero_serie in numeros_encontrados:
        print(f"{archivo}\t\t{numero_serie}")
    print("\nNúmeros encontrados:", len(numeros_encontrados))
    print("Duración de la búsqueda:", duracion_busqueda, "segundos")
    print("-" * 50)


# Directorio raíz donde se realizará la búsqueda
directorio_raiz = "C:\\Users\\ruben\\Desktop\\CURSO PYTHON\\DIA 9\\Mi_Gran_Directorio"

# Llamar a la función para buscar los números de serie
buscar_numeros_serie(directorio_raiz)