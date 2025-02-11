import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

class GoogleSearch:
    def __init__(self, query, site):
        self.query = query
        self.site = site
        self.url = f'https://www.google.com/search?q={self.query}+{self.site}'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    def search(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            
            if response.status_code == 200:
                return self.parse_results(response.text)
            else:
                # Lança uma exceção com a mensagem de erro detalhada
                raise Exception(f"Erro ao realizar a pesquisa: {self.query} | Código de status: {response.status_code} | Conteúdo da resposta: {response.text}")
            
        except requests.exceptions.RequestException as e:
             # Captura erros relacionados à requisição e lança uma exceção
            raise Exception(f"Erro ao fazer a requisição: {e}")
        
    def parse_results(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        results = []

        for result in soup.find_all('h3'):
            link = result.find_parent('a')['href']

            # Filtrar apenas links que contêm "/musica/"
            if "/musica/" in link:
                # Decodificar o link para lidar com caracteres especiais
                decoded_link = unquote(link)

                # Extrair o nome da música do link
                music_name = decoded_link.split("/musica/")[1].replace('-', ' ').strip('/').title()

                # Adicionar o dicionário com nome e link à lista de resultados
                results.append({'name': music_name, 'link': link})
        
        return results

# Exemplo de uso:
if __name__ == '__main__':
    query = 'santo'
    site = 'site:musicasparamissa.com.br'
    
    google_search = GoogleSearch(query, site)
    links = google_search.search()
    
    for link in links:
        print(f"Link: {link}")
