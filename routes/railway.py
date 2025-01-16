from railway_env_tester import RailwayEnvTester
from flask import Blueprint, jsonify

railway_bp = Blueprint('railway', __name__)

@railway_bp.route('/railway', methods=['GET'])
def railway_env_tester():
    try:
        tester = RailwayEnvTester()

        # Carregar as variáveis de ambiente
        tester.load_env_variables()

        # Verificar se as variáveis de ambiente estão corretas
        tester.check_env_variables()

        # Exibir todas as variáveis de ambiente
        tester.print_all_env_variables()

        return "teste executado, verifique os logs"
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        # Retorna o erro como resposta JSON, com código 500 para erro interno
        return jsonify({'error': str(e)}), 500
    
