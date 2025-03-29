from bs4 import BeautifulSoup
import os
import zipfile
import urllib.request

def GetChosenLinks(soup, count):
    """Permite que o usuário digite os textos dos links que deseja baixar e retorna os links correspondentes."""
    links = soup.find_all("a", href=True)
    chosen_links = []
    
    for i in range(count):
        print(f"\nEscolha o link {i+1}:")
        link_text = input("Digite o texto do anexo que você quer baixar: ").strip()
        found = False
        
        for link in links:
            text = link.get_text().strip()
            if link_text.lower() in text.lower():  # Verifica se o texto corresponde
                href = link['href']
                if not href.startswith("http"):
                    href = "https://www.gov.br" + href
                print(f"Link encontrado: {text} -> {href}")
                chosen_links.append(href)
                found = True
                break  # Sai do loop quando encontra o link
        
        if not found:
            print(f"Nenhum link encontrado para o texto: '{link_text}'")
    
    return chosen_links


def DownloadContent(url, filename="Anexo"):
    """Baixa o conteúdo do link e salva no arquivo especificado."""
    try:
        extension = url.split('.')[-1]
        file_path = f"{filename}.{extension}"

        print(f"Baixando o arquivo de: {url}")
        urllib.request.urlretrieve(url, file_path)
        print(f"Arquivo salvo como: {file_path}")
        return file_path  # Retorna o caminho do arquivo salvo
    except Exception as e:
        print(f"Erro ao baixar o arquivo: {e}")
        return None

def GenerateZip(files, zip_name="Anexos.zip"):
    """Cria um arquivo ZIP com os arquivos baixados."""
    try:
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            for file in files:
                zipf.write(file, os.path.basename(file))  # Adiciona ao ZIP
                print(f"Arquivo {file} adicionado ao ZIP.")
        print(f"Arquivo ZIP criado com sucesso: {zip_name}")
    except Exception as e:
        print(f"Erro ao criar o arquivo ZIP: {e}")

# function to find all links in a webpage and print them
def ChooseLinks(soup):
    """Exibe todos os links encontrados na página fornecida."""
    links = soup.find_all("a", href=True)
    for link in links:
        href = link['href']
        text = link.get_text().strip()
        href = FormatLink(href)

# function to format link ensuring it has the full domain
def FormatLink(href):
    """Formata o link para garantir que tenha um domínio completo."""
    if not href.startswith("http"):
        href = "https://www.gov.br" + href
    return href

# function to get link based on user input
def FindLink(links, choice):
    """Busca o link pelo texto fornecido, passe o parâmetro que mostra todos os links seguido do texto que se assemelha ao 
    que está no conteúdo do HTML da página."""
    for link in links:
        text = link.get_text().strip()
        if choice.lower() in text.lower():
            return link['href']
    return None

# function to get link href and return it for webscraping unit testing
def GetRef(soup):
    """Permite escolher um link pelo texto e retorna o link completo. Passe o parâmetro que manipula o HTML"""
    links = soup.find_all("a", href=True) # get all links from page 
    while True:
        choice = input("Digite o texto do anexo que você quer baixar: ").strip()
        href = FindLink(links, choice)
        if href:
            href = FormatLink(href)
            print(f"Link encontrado: {choice} -> {href}")
            return href
        print("Não encontrei um link com esse nome, tente novamente.")
