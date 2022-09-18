from Exercicio4 import dic_ano

meses = list(dic_ano.keys())
dias = list(dic_ano.values())
for i in range (len(dic_ano)):
    print(meses[i],"-", dias[i])