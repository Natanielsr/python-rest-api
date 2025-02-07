from bs4 import BeautifulSoup
import requests
from services.lyric_extractor_abstract_factory.lyric_extractor import LyricExtractor
from services.lyric_extractor_abstract_factory.lyric_extractor_factory import LyricExtractorFactory

class LyricExtractorMusicasParaMissaFactory(LyricExtractorFactory):
    def create_extractor(self):
        return LyricExtractorMusicasParaMissa()

class LyricExtractorMusicasParaMissa(LyricExtractor):
    def get_lyric(self, url : str) -> str:
        try:
            self.fetch_lyric(url)
        except requests.RequestException as e:
            raise RuntimeError(f"Erro ao fazer a requisição para a URL: {e}")
        except Exception as e:
            raise RuntimeError(f"Erro ao extrair a letra da música: {e}")

        return self.lyric
    
    def fetch_lyric(self, url):
        # Fazer a requisição para a página
        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Procurar o elemento que contém a letra da música
        lyric_div = soup.find('div', id='div-letra')  # Altere 'letra' para a classe correta
        
        # Extrair o texto da letra
        if lyric_div:
            for br_tag in lyric_div.find_all('br'):
                br_tag.replace_with('\n')
            self.lyric = lyric_div.get_text().strip()
        else:
            raise ValueError("Elemento contendo a letra da música não encontrado")

# Exemplo de uso:
if __name__ == '__main__':
    # URL da página
    url = 'https://musicasparamissa.com.br/musica/santo-leo-mantovani/'

    # Criando uma instância da classe e extraindo a letra
    lyrics_extractor = LyricExtractorMusicasParaMissa()
    print(lyrics_extractor.get_lyric(url))