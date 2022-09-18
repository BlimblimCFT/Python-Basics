from asyncore import write
import csv

with open("alunos_copia.csv", 'w', newline='', encoding='utf-8') as copia:
    escritor = csv.writer(copia)
    with open("alunos.csv", 'r', encoding='utf-8') as alunos_csv:
        reader = csv.reader(alunos_csv)
        for i in reader:
                escritor.writerow(i)

with open("alunos_media.csv", 'w', newline='', encoding='utf-8') as media:
     escritor = csv.writer(media)
     with open("alunos.csv", 'r', encoding='utf-8') as alunos_csv:
        reader = csv.reader(alunos_csv)
        header = next(reader)
        header.append('Media')
        escritor.writerow(header)
        for i in reader:
                for num in range(3, 7):
                    i[num] = float(i[num])
                i.append(sum(i[3:7])/4)
                escritor.writerow(i)

                