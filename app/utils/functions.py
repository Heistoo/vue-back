from bs4 import BeautifulSoup

# function to find all links in a webpage and print them
def ChooseLinks(soup):
    """Exibe todos os links encontrados na página."""
    links = soup.find_all("a", href=True)
    for link in links:
        href = link['href']
        text = link.get_text().strip()
        href = FormatLink(href)
        print(f"Texto: {text} -> Link: {href}")

def FormatLink(href):
    """Formata o link para garantir que tenha o domínio completo."""
    if not href.startswith("http"):
        href = "https://www.gov.br" + href
    return href

def FindLink(links, choice):
    """Busca o link pelo texto fornecido."""
    for link in links:
        text = link.get_text().strip()
        if choice.lower() in text.lower():
            return link['href']
    return None

def GetRef(soup):
    """Permite escolher um link pelo texto e retorna o link completo."""
    links = soup.find_all("a", href=True)
    while True:
        choice = input("Digite o texto do anexo que você quer baixar: ").strip()
        href = FindLink(links, choice)
        if href:
            href = FormatLink(href)
            print(f"Link encontrado: {choice} -> {href}")
            return href
        print("Não encontrei um link com esse nome, tente novamente.")
