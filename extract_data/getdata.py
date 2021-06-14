from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from urllib.error import HTTPError
import re
import csv
import time

with open('booklinks.csv', 'r') as f:

    lista = f.read().splitlines()

    for line in lista:

        try:
            uClient = uReq(line)
        except:
            time.sleep(30)
            print("Problemas con: " + line)
            uClient = uReq(line)

        web = soup(uClient.read(), 'html.parser')
        uClient.close()
        
        b_title = ""
        b_author = ""
        b_pages = ""
        b_year = ""
        b_ratings = ""
        b_avr_rating = ""

        try:
            b_title = (web.find('h1', class_='gr-h1 gr-h1--serif')).text.strip("\n").lstrip(" ")
        except: pass

        try:
            b_author = (web.find('a', class_='authorName')).text
        except: pass

        try:
            b_pages = (web.find('span', itemprop='numberOfPages')).text.replace(" pages", "")
        except: pass

        try:
            b_ratings = web.find(itemprop='ratingCount').get('content')
        except: pass

        try:
            b_avr_rating = (web.find('span', itemprop='ratingValue')).text.strip("\n")
        except: pass

        try:
            b_year = str(re.findall(r'(\d{3,4})', str((web.find('nobr', class_='greyText')).text))).strip("['']")
        except AttributeError:
            try:
                b_year = str(re.findall(r'(\d{3,4})', str((web.findAll('div', class_='row'))[1].text))).strip("['']")
            except: pass
        except: pass
            
        b_genres = []

        try:
            for g in web.findAll('a', class_='actionLinkLite bookPageGenreLink'):
                tag = g.get('href').replace("/genres/", "")
                b_genres.append(tag)
        except: pass

        if b_title == "": b_title = "No encontrado"
        elif b_author == "": b_author = "No encontrado"
        elif b_pages == "": b_pages = "No encontrado"
        elif b_year == "": b_year = "No encontrado"
        elif b_genres == "": b_genres = "No encontrado"
        elif b_ratings == "": b_ratings = "No encontrado"
        elif b_avr_rating == "": b_avr_rating = "No encontrado"

        book_added = b_title, b_author, b_pages, b_year, b_genres, b_ratings, b_avr_rating, line

        with open('goodreadsdb.csv', 'a', newline='', encoding='utf-8') as adding:
            writer = csv.writer(adding)
            writer.writerow(book_added)
            adding.close()
