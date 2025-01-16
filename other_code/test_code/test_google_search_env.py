import os

api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
search_engine_id = os.getenv("GOOGLE_SEARCH_ENGINE_ID")

if api_key and search_engine_id:
    print("As variáveis de ambiente estão configuradas.")
else:
    print("As variáveis de ambiente não estão configuradas corretamente.")
