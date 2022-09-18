from urllib import request
import requests
url = "https://api.exchangerate-api.com/v6/latest"
req = requests.get(url)

dados = req.json()

valor_reais = float(input("Informe o valor em reais a ser convertido\n"))
cotacao = dados['rates']['BRL']
print(f'R${(valor_reais):.2f} em dólar valem US${(valor_reais/cotacao):.2f}')