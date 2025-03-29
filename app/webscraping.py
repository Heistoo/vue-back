from urllib.request import urlopen
from bs4 import BeautifulSoup
from utils.functions import ChooseLinks, GetRef

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# Chamando as funções do arquivo utils/functions.py
# ChooseLinks(soup)
verify = False
while not verify:
    try:
        count = int(input("Quantos links você quer baixar? "))
        if count > 0:
            print("\nEscolha os links pelo texto:")
            for _ in range(count):
                GetRef(soup)
            verify = True
        else:
            print("Digite um número maior que 0")
    except ValueError:
        print("Por favor, digite um número válido.")