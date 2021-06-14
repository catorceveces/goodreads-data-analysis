# Obtención de base de datos para posterior manipulación.

## Base de Datos de Goodreads:

A través de getlinks.py obtenemos los links de los diez mil libros iniciales correspondientes a la lista "Best Books Ever" de Goodreads (a fecha 30/05/2021). Procedemos de este modo a raíz de que scrapear cada libro individualmente en una única operación demora algunos días - teniendo que respetar el rate limit de Goodreads, y durante ese lapso de tiempo la lista puede sufrir alguna variación. Así, en pocos minutos adquirimos los diez mil links que, más adelante, y con los tiempos adecuados, scrapearemos en detalle.

getlinks.py dará como resultado un archivo csv con el listado de links (booklinks.csv). Ese archivo será la base de getdata.py.

## ¿Qué datos de relevancia serán extraídos?

De cada uno de los diez mil libros, recabaremos:

* Título.
* Autor.
* Cantidad de páginas.
* Año de publicación.
* Rating.
* AVR Rating.

En caso de que no sean halladas, a cada una de estas variables le será asignado un valor de "No encontrado", con el que trabajaremos más adelante.

## Jupyter Notebook para filtrado.

Con la base de datos en bruto goodreadsdb.csv, creamos una libreta de Jupyter. En ella, construimos el DataFrame y filtramos aquellos libros que posean variable de "No encontrado". Vemos que no existen libros que cumplan ese criterio para las variables Título y Autor. Sin embargo, sí hay para Cantidad de páginas y Año de publicación.

Con las herramientas que nos provee la librería Pandas, generamos dos nuevos archivos csv: uno para los libros sin cantidad de páginas asignadas y otro para los libros sin fecha de publicación.

## Otras fuentes.

Utilizamos cleanpagesdata.py y cleanyearsdata.py para buscar los datos que no pudimos obtener a través de Goodreads. Empleamos como fuente otras dos webs ampliamente documentadas en literatura: BookDepository y WorldCat. En la medida en que los libros de los que necesitamos información extra son escasos, efectuaremos un chequeo manual, libro a libro, de la información que sea scrapeada de estos dos sitios. Decidiremos individualmente.

Se generarán dos archivos csv: noyearcleaned.csv y nopagescleaned.csv.

### Aclaración:

Algunos de los libros sin fecha de publicación corresponden a autores clásicos como Séneca o Virgilio. En estos casos, asignamos valor 0 al año de publicación. Ello, debido a que al trabajar posteriormente con la base de datos final tomaremos como parámetro de análisis la invención de la imprenta (año 1440 d. C.).

## Base de Datos final:

Para la base de datos final que será objeto de análisis tomaremos como base los archivos csv:

* goodreadsdb.csv.
* noyearcleaned.csv.
* nopagescleaned.csv.

Con finaldatabase.py creamos el archivo definitivo con el que efectuaremos los análisis.
