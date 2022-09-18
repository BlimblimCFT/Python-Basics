print("Responda as próximas perguntas com SIM ou NÃO:")
pontos = 0
a = input("\nMora perto da vítima? ")
while (a.lower()!="sim" and a.lower()!='não'):
    print("\nResponda com SIM ou NÃO")
    a = input("\nMora perto da vítima? ")
b = input("\nJá trabalhou com a vítima? ")
while (b.lower()!="sim" and b.lower()!='não'):
    print("\nResponda com SIM ou NÃO")
    b = input("\nJá trabalhou com a vítima? ")
c = input("\nTelefonou para a vítima? ")
while (c.lower()!="sim" and c.lower()!='não'):
    print("\nResponda com SIM ou NÃO")
    c = input("\nTelefonou para a vítima? ")
d = input("\nEsteve no local do crime? ")
while (d.lower()!="sim" and d.lower()!='não'):
    print("\nResponda com SIM ou NÃO")
    d = input("\nEsteve no local do crime? ")
e = input("\nDevia para a vítima? ")
while (e.lower()!="sim" and e.lower()!='não'):
    print("\nResponda com SIM ou NÃO")
    e = input("\nDevia para a vítima? ")

if (a == 'sim'):
    pontos+=1
if (b == 'sim'):
    pontos+=1
if (c == 'sim'):
    pontos+=1
if (d == 'sim'):
    pontos+=1
if (e == 'sim'):
    pontos+=1


if(pontos == 5):
    print("\nAssassino")
elif(pontos >=3):
    print("\nCúmplice")
elif(pontos == 2):
    print("\nHmmmmm, suspeito")
else:
    print("\nLiberado")

