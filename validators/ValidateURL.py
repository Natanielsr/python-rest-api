from urllib.parse import urlparse


class ValidateURL:
    validsURL = ['https://musicasparamissa.com.br/musica/']

    def __init__(self):
        pass

    @staticmethod
    def is_valid(url : str) -> bool:
        for valids_url in ValidateURL.validsURL:
            if url.startswith(valids_url):
                return True
        return False