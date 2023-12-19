import bs4
import requests

#CREAR UNA URL SIN NUMERO DE PAGINA

url_base = "https://books.toscrape.com/catalogue/page-{}.html"

#LISTA DE TITULOS CON 4 O 5 ESTRELLAS

titulos_rating_alto = []

#iterar paginas

for pagina in range(1,51):
    #crear sopa en cada pagina.
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text,"lxml")

    #seleccionar datos de los libros.
    libros = sopa.select(".product_pod")

    #iterar libros
    for libro in libros:

        #chequear que tengan 4 o 5 estrellas.
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:

            #guardar título en variable.
            titulo_libro = libro.select("a")[1]["title"]

            #agregar libro a la lista.
            titulos_rating_alto.append(titulo_libro)

# ver libros de 4 y 5 estrellas en consola.

for t in titulos_rating_alto:
    print(t)



