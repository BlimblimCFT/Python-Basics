def somalistas(lista1, lista2):
    if (len(lista1) > len(lista2)):
        size = len(lista1)
    elif (len(lista1) < len(lista2)):
        size = len(lista2)
    else:
        size = len(lista1)
    for i in range(size):
        lista3.append(lista1[i] + lista2[i])
    return lista3

lista3 = []
somalistas(lista1=[1,4, 3], lista2=[3,5,1])
print(lista3)