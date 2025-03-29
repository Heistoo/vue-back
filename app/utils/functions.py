from bs4 import BeautifulSoup
import os
import zipfile
import urllib.request

# function to reduce code reutilization by verifying directory existence
def EnsureDirectoryExists(directory):
    """Verifica se o diretório existe e, caso contrário, cria-o."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Diretório {directory} criado.")
    else:
        print(f"Diretório {directory} já existe.")


# function to get links from user input and store in a list
def GetChosenLinks(soup, count):
    """Permite que o usuário escolha os links para baixar e retorna os links selecionados."""
    chosen_links = []

    for i in range(count):
        print(f"\nEscolha o link {i+1}:")
        link = GetRef(soup)  # utilize getref to get the link from the user
        if link:
            chosen_links.append(link)
    return chosen_links

# function to download content from given link and save it to a file in raw folder (for pdfs, xlsx, etc)
def DownloadContent(url, filename="Anexo", save_directory="data/raw"):
    """Baixa o conteúdo do link e salva no arquivo especificado dentro do diretório informado."""
    try:
        # verify if directory exists
        EnsureDirectoryExists(save_directory)

        extension = url.split('.')[-1]
        file_path = os.path.join(save_directory, f"{filename}.{extension}")  # Usando o caminho completo

        print(f"Baixando o arquivo de: {url}")
        urllib.request.urlretrieve(url, file_path)
        print(f"Arquivo salvo como: {file_path}")
        return file_path  # Retorna o caminho do arquivo salvo
    except Exception as e:
        print(f"Erro ao baixar o arquivo: {e}")
        return None


# function to generate a zip file for downloaded files
def GenerateZip(files, zip_name="Anexos.zip", save_directory="data/processed"):
    """Cria um arquivo ZIP com os arquivos baixados."""
    try:
        # verify if directory already exists
        EnsureDirectoryExists(save_directory)
        
        zip_path = os.path.join(save_directory, zip_name)

        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file in files:
                zipf.write(file, os.path.basename(file))  # add files to zip
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
