from tester.env_tester import EnvTester
from flask import Blueprint, jsonify

tester_bp = Blueprint('tester', __name__)

@tester_bp.route('/tester/envtest', methods=['GET'])
def railway_env_tester():
    try:
        tester = EnvTester()

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
    
