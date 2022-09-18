import csv

with open("Let's Code/Python Basics/Módulo 3/brasil_covid.csv", 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    next(leitor)
    for i in leitor:
        if float(i[2]) > 30000:
            print(i)
        
with open('users_csv', 'w', encoding='utf-8', newline='') as arquivos_users:
    escritor = csv.writer(arquivos_users)
    escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
    escritor.writerow(['Pietro', 'Ribeiro', 'pietro@email.com', 'masculino'])
