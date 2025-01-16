import os

class RailwayEnvTester:
    def __init__(self):
        self.api_key = None
        self.search_engine_id = None

    def load_env_variables(self):
        # Acessar as variáveis de ambiente
        self.api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
        self.search_engine_id = os.getenv("GOOGLE_SEARCH_ENGINE_ID")

    def check_env_variables(self):
        # Verificar se as variáveis estão sendo lidas corretamente
        if self.api_key and self.search_engine_id:
            print("Variáveis de ambiente carregadas com sucesso!")
            print(f"API Key: {self.api_key}")
            print(f"Search Engine ID: {self.search_engine_id}")
        else:
            print("Erro: Não foi possível acessar as variáveis de ambiente.")
            print("Certifique-se de que as variáveis de ambiente 'GOOGLE_SEARCH_API_KEY' e 'GOOGLE_SEARCH_ENGINE_ID' estão definidas corretamente no painel do Railway.")

    def print_all_env_variables(self):
        # Exibir todas as variáveis de ambiente (para depuração)
        print("\n--- Todas as variáveis de ambiente ---")
        for key, value in os.environ.items():
            print(f"{key}: {value}")

# Testando a classe
if __name__ == "__main__":
    tester = RailwayEnvTester()

    # Carregar as variáveis de ambiente
    tester.load_env_variables()

    # Verificar se as variáveis de ambiente estão corretas
    tester.check_env_variables()

    # Exibir todas as variáveis de ambiente
    tester.print_all_env_variables()
