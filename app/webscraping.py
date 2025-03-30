from urllib.request import urlopen
from bs4 import BeautifulSoup
from app.utils.scrapingfunctions import ChooseLinks, GetRef, DownloadContent, GenerateZip, GetChosenLinks

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

try:
    count = int(input("\nQuantos links você quer escolher? "))
    if count > 0:
        
        # get links based on the user numerical input
        chosen_links = GetChosenLinks(soup, count)

        # download files from given link
        downloaded_files = []  # Lista para armazenar os arquivos baixados
        for i, link in enumerate(chosen_links, 1):
            file_path = DownloadContent(link, f"Anexo_{i}")
            if file_path:
                downloaded_files.append(file_path)

        # integration with downloaded files to compact in a zip file
        if downloaded_files:
            GenerateZip(downloaded_files, "anexos.zip")
    else:
        print("Digite um número maior que 0")
except ValueError:
    print("Por favor, digite um número válido.")