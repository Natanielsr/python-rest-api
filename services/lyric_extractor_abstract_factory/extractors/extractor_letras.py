from bs4 import BeautifulSoup
import requests

from services.lyric_extractor_abstract_factory.lyric_extractor import LyricExtractor
from services.lyric_extractor_abstract_factory.lyric_extractor_factory import LyricExtractorFactory

class LyricExtractorLetrasFactory(LyricExtractorFactory):
    def create_extractor(self):
        return LyricExtractorLetras()

class LyricExtractorLetras(LyricExtractor):
    def get_lyric(self, url : str):
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            div_lyrics = soup.find('div', class_='lyric-original')
            if div_lyrics:
                paragrafos = div_lyrics.find_all('p')
                n_par = len(paragrafos)
                count = 0
                lyric = ''
                for p in paragrafos:
                    texto = p.get_text(separator="\n")
                    lyric += texto
                    if count < n_par - 1:
                        lyric += '\n\n'
                    count += 1

                return lyric
            else:
                raise Exception(f"Div com a classe 'lyric-original' não encontrada em '{url}'.")
        else:
            raise Exception(f"Erro ao acessar a página '{url}' : {response.status_code}")