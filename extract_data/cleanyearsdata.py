from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from urllib.error import HTTPError
import re
import csv
import time

with open('noyear.csv', 'r') as f:

    csv_reader = csv.reader(f)

    for l in csv_reader:

        name = l[0].replace(" ", "+")
        author = l[1].replace(" ", "+")

        terms = name + "+" + author
        terms = terms.encode("ascii", 'replace').decode()

        bookdep = 'https://www.bookdepository.com/es/search?searchTerm={}&search=Find+book'.format(terms)

        uClient = uReq(bookdep)
        web =soup(uClient.read(), 'html.parser')
        uClient.close()

        print("Buscando en BookDepository..")

        try:
            b_year = str(re.findall('\d{3,4}', (web.find('span', itemprop='datePublished')).text.replace("\n", " ")))
        except:
            b_year = "No encontrado"
            pass

        if b_year == "No encontrado":

            print("No encontrado en BookDepository. Buscando en WorldCat..")

            worldcat = 'https://www.worldcat.org/search?q={}&qt=results_page'.format(terms)

            uClient = uReq(worldcat)
            web =soup(uClient.read(), 'html.parser')
            uClient.close()

            try:
                worldcatlink = (web.find('a', id='result-1')).get('href')
                worldcatlink = "https://www.worldcat.org/" + worldcatlink

                uClient = uReq(worldcatlink)
                web =soup(uClient.read(), 'html.parser')
                uClient.close()

                try:
                    b_year = str(re.findall('\d{3,4}', (web.find('td', id='bib-publisher-cell')).text.replace("\n", " ")))

                    if b_year == "[]" or b_year == "":
                        b_year = "No encontrado"

                except:
                    b_year = "No encontrado"
                    pass
            except:
                pass

        print("Se encontró el valor de b_year: " + str(b_year) + " para el libro: " + l[0] + " de " + l[1] + ". ¿Es correcto?")
        print("A: Es correcto.\nB: No. Ingresar manualmente.\n")
        option = input("Ingrese su opción: ")

        if option == "A":
            pass
        else:
            val = input("Ingrese su valor: ")
            b_year = str(val)

        clean_book = l[0], l[1], l[2], b_year, l[4], l[5], l[6], l[7]

        with open('noyearcleaned.csv', 'a', newline='', encoding='utf-8') as adding:
            writer = csv.writer(adding)
            writer.writerow(clean_book)
            adding.close()

        print("\n")

        time.sleep(3)


f.close()
