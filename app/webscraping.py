from urllib.request import urlopen
from bs4 import BeautifulSoup
from utils.functions import ChooseLinks, GetRef, DownloadContent, GenerateZip, GetChosenLinks

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# Chamando as funções do arquivo utils/functions.py
# ChooseLinks(soup)

try:
    count = int(input("\nQuantos links você quer escolher? "))
    if count > 0:
        # Obter os links escolhidos pelo usuário
        chosen_links = GetChosenLinks(soup, count)

        # Baixar os arquivos
        downloaded_files = []  # Lista para armazenar os arquivos baixados
        for i, link in enumerate(chosen_links, 1):
            file_path = DownloadContent(link, f"downloaded_file_{i}")
            if file_path:
                downloaded_files.append(file_path)

        # Compactar todos os arquivos baixados em um arquivo ZIP
        if downloaded_files:
            GenerateZip(downloaded_files, "downloads.zip")
    else:
        print("Digite um número maior que 0")
except ValueError:
    print("Por favor, digite um número válido.")