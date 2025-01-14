import requests
from bs4 import BeautifulSoup

class GoogleSearch:
    def __init__(self, query, site):
        self.query = query
        self.site = site
        self.url = f'https://www.google.com/search?q={self.query}+{self.site}'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    def search(self):
        response = requests.get(self.url, headers=self.headers)
        
        if response.status_code == 200:
            return self.parse_results(response.text)
        else:
            print("Erro ao realizar a pesquisa")
            return []
    
    def parse_results(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        results = []

        for result in soup.find_all('h3'):
            link = result.find_parent('a')['href']
            results.append(link)
        
        return results

# Exemplo de uso:
if __name__ == '__main__':
    query = 'pelas estradas da vida'
    site = 'site:musicasparamissa.com.br'
    
    google_search = GoogleSearch(query, site)
    links = google_search.search()
    
    for link in links:
        print(f"Link: {link}")
