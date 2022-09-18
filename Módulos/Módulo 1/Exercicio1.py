valor = input("Insira um valor monetário: ")
while (valor.isdigit()== 0):
    print("O valor precisa ser inteiro, tente novamente")
    valor = input("Insira um valor monetário: ")
print("O novo valor é: ", (float(valor)*0.85))