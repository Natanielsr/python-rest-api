import requests
import json

json_path = './googleSearchApiKey.json'

with open(json_path, 'r') as file:
    data = json.load(file)

API_KEY = data['apiKey']
SEARCH_ENGINE_ID = data['searchEngineID']

print("ApiKey: ", API_KEY)
print("Search Engine ID: ", SEARCH_ENGINE_ID)

search_query = "Amém"

url = 'https://www.googleapis.com/customsearch/v1'
params = {
    'q' : search_query,
    'key': API_KEY,
    'cx': SEARCH_ENGINE_ID
}

response = requests.get(url, params=params)
results = response.json()

if 'items' in results:
    items = results['items']
    for item in items:
        print(item['link'])
    
