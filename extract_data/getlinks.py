from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv
import time

page = 1

while page != 101:

    time.sleep(1)
    gr_list = 'http://www.goodreads.com/list/show/1.Best_Books_Ever?page={}'.format(page)

    try:
        uClient = uReq(gr_list)
    except:
        time.sleep(20)
        print("Problemas con página " + str(page))
        uClient = uReq(gr_list)

    web = soup(uClient.read(), 'html.parser')
    uClient.close()

    books = web.findAll('a', class_='bookTitle')

    for b in books:

        link = b.get('href')
        book_link = 'http://www.goodreads.com'+link


        with open('booklinks.csv', 'a', newline='') as adding:
            writer = csv.writer(adding)
            writer.writerow([book_link])
            adding.close()

    print("Fin de página " + str(page))

    page = page + 1
