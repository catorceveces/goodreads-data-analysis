import csv

with open('database.csv', 'a', newline='', encoding='utf-8') as final:

    writer = csv.writer(final)

    with open('goodreadsdb.csv', 'r') as f:

        f_reader = csv.reader(f)

        for l in f_reader:

            if l[2] == "No encontrado":

                with open('nopagescleaned.csv', 'r') as p:

                    p_reader = csv.reader(p)

                    for x in p_reader:

                        if x[7] == l[7]:

                            l[2] = x[2]

            if l[3] == "No encontrado":

                with open('noyearcleaned.csv', 'r') as y:

                    y_reader = csv.reader(y)

                    for z in y_reader:

                        if z[7] == l[7]:

                            l[3] = z[3]

            final_book = str(l[0]), str(l[1]), int(l[2].strip("[]").replace("'", "").replace(" ", "")), int(l[3].strip("[]").replace("'", "").replace(" ", "")), l[4].strip("[]").replace("'", "").replace(" ", "").split(","), int(l[5]), float(l[6]), str(l[7])

            writer.writerow(final_book)

final.close()
p.close()
y.close()
