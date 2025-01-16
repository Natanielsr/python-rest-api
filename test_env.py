import os

from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
print(dotenv_path)

load_dotenv(dotenv_path)

GOOGLE_SEARCH_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")

print(GOOGLE_SEARCH_API_KEY)