a = input("Insira uma idade entre 0 e 150: ")
b = input("Insira um salário maior que 0: ")
c = input("Insira um sexo, M, F ou Outro: ")
while (a.isdigit()== 0):
    print("A idade precisa ser um numero, tente novamente")
    a = input("Insira uma idade entre 0 e 150: ")
while (b.isdigit()== 0):
    print("O salario precisa ser um numero maior que 0, tente novamente")
    b = input("Insira um salario maior que 0: ")
if (((int(a)>=0) and (int(a)<=150)) == 0):
    print("A idade inserida não é válida")
else:
    print("A idade é: ", a)
if ((int(b)>0) == 0):
    print("O salário é inválido ou o trabalho é escravo")
else:
    print("O salário é: ", b)
if (((c.lower()!='m') and (c.lower()!='f') and (c.lower()!='outro'))):
    print("O sexo inserido não corresponde a M, F ou Outro")
else: 
    print("O sexo é:", c.capitalize())