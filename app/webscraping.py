from urllib.request import urlopen
from bs4 import BeautifulSoup
from utils.functions import ChooseLinks, GetRef

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# Chamando as funções do arquivo utils/functions.py
print("Listando todos os links da página:")
ChooseLinks(soup)

print("\nEscolha um link pelo texto:")
GetRef(soup)
