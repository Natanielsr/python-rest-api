import requests
import json
from urllib.parse import unquote
import os

class GoogleSearchAPI:
    def __init__(self):
        self.json_path = './googleSearchApiKey.json'
        #self.api_key, self.search_engine_id = self.load_api_key(self.json_path)
        self.api_key, self.search_engine_id = self.load_api_key()
        self.url = 'https://www.googleapis.com/customsearch/v1'

    def load_api_key(self):
        api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
        search_engine_id = os.getenv("GOOGLE_SEARCH_ENGINE_ID")

        if not api_key or not search_engine_id:
            raise ValueError("Chave de API ou ID do mecanismo de pesquisa não configurados corretamente. "
                             "Verifique as variáveis de ambiente 'GOOGLE_SEARCH_API_KEY' e 'GOOGLE_SEARCH_ENGINE_ID'.")

        return api_key, search_engine_id
        
    def load_api_key_json(self, json_path):
        try:
            with open(json_path, 'r') as file:
                data = json.load(file)
            return data['apiKey'], data['searchEngineID']
        except (FileNotFoundError, KeyError) as e:
            raise Exception(f"Erro ao carregar o arquivo JSON: {e}")

    def search(self, query):
        if not self.api_key or not self.search_engine_id:
            raise Exception("Chave de API ou ID do mecanismo de pesquisa não configurados corretamente.")
        
        params = {
            'q': query,
            'key': self.api_key,
            'cx': self.search_engine_id
        }

        try:
            return self.try_request(params)
        except requests.RequestException as e:
            raise Exception(f"Erro ao fazer a requisição: {e}")
        
    def try_request(self, params):
        response = requests.get(self.url, params=params)
        response.raise_for_status()
        results = response.json()
        
        if 'items' in results:
            items = results['items']
            musics = []
            #print(items)
            for item in items:
                link = item['link']
                title : str = item['title']
                name = title.replace(" - Músicas para Missa", "")

                musics.append(self.create_obj(link, name))

            return musics
        else:
            return ["Nenhum resultado encontrado."]

    def create_obj(self, link, name):
        return {'name': name, 'link': link}

# Exemplo de uso
if __name__ == "__main__":
    search_api = GoogleSearchAPI()
    result = search_api.search("Amém")
    print(result)
