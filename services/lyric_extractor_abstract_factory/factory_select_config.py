from urllib.parse import urlparse

from services.lyric_extractor_abstract_factory.extractors.extractor_letras import LyricExtractorLetrasFactory
from services.lyric_extractor_abstract_factory.extractors.extractor_musicas_para_missa import LyricExtractorMusicasParaMissaFactory

class FactorySelectConfig:

    URLs = {
        'musicasparamissa': 'https://musicasparamissa.com.br/musica/',
        'letrasmus': 'https://www.letras.mus.br/',
    }

    def select(self, url: str):
        host_name = self.get_host_name(url)
        match host_name:
            case "musicasparamissa":
                return LyricExtractorMusicasParaMissaFactory()
            case "letrasmus":
                return LyricExtractorLetrasFactory()
            case _:
                raise ValueError("URL not found in lyric extractor factory select")


    def get_host_name(self, url: str) -> str:
        parsed_url = urlparse(url)
        for name, valids_url in self.URLs.items():
            if parsed_url.netloc == urlparse(valids_url).netloc:
                return name
        return None