import requests
from bs4 import BeautifulSoup

class LyricExtractor:
    def __init__(self, url):
        self.url = url
        self.lyric = None
    
    def fetch_lyric(self):
        if not self.is_valid_url():
            self.lyric = f'endereço da música inválido'
            return
        
        # Fazer a requisição para a página
        response = requests.get(self.url)

        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Procurar o elemento que contém a letra da música
        lyric_div = soup.find('div', id='div-letra')  # Altere 'letra' para a classe correta
        
        # Extrair o texto da letra
        if lyric_div:
            for br_tag in lyric_div.find_all('br'):
                br_tag.replace_with('\n')
            self.lyric = lyric_div.get_text().strip()
        else:
            self.lyric = "Não foi possível encontrar a letra da música."
    
    def get_lyric(self):
        if self.lyric is None:
            self.fetch_lyric()
        return self.lyric
    
    def is_valid_url(self):
        # Verificar se a URL começa com o prefixo desejado
        prefix = 'https://musicasparamissa.com.br/musica/'
        if self.url.startswith(prefix):
            return True
        return False

# Exemplo de uso:
if __name__ == '__main__':
    # URL da página
    url = 'https://musicasparamissa.com.br/musica/santo-leo-mantovani/'

    # Criando uma instância da classe e extraindo a letra
    lyrics_extractor = LyricExtractor(url)
    print(lyrics_extractor.get_lyrics())
