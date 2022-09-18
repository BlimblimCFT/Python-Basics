lista = [2, 3, 4, 5, 10, 12, 14, 13, 11, 9, 7, 6]
size = len(lista)
pares = 0
for i in range(size):
    if ((lista[i] % 2) == 0):
        pares+=1
print("A quantia de itens pares é: ", pares)