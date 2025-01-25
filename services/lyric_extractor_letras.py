import requests
from bs4 import BeautifulSoup

class LyricExtractorLetras:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def get_lyric(self, url):
        response = requests.get(url, headers=self.headers)
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
        
if __name__ == '__main__':
    # Exemplo de uso
    url = "https://www.letras.mus.br/ministerio-amor-e-adoracao/gloria-a-deus-nas-alturas/"
    extractor = LyricExtractorLetras()
    print(extractor.get_lyric(url))