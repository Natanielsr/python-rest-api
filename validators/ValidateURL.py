from urllib.parse import urlparse


class ValidateURL:
    validsURL = {
        'musicasparamissa': 'https://musicasparamissa.com.br/musica/',
        'letrasmus': 'https://www.letras.mus.br/',
    }

    def __init__(self):
        pass

    @staticmethod
    def is_valid(url : str) -> bool:
        for valids_url in ValidateURL.validsURL.items():
            if url.startswith(valids_url):
                return True
        return False
    
    @staticmethod
    def get_host_name(url: str) -> str:
        parsed_url = urlparse(url)
        for name, valids_url in ValidateURL.validsURL.items():
            if parsed_url.netloc == urlparse(valids_url).netloc:
                return name
        return None