from flask import Blueprint, jsonify
from services.google_search_api import GoogleSearchAPI

search_bp = Blueprint('search', __name__)


@search_bp.route('/search/<string:query>', methods=['GET'])
def get_search_results(query):
    try:
        search_api = GoogleSearchAPI()
        result = search_api.search(query)

        return jsonify({'results': result})
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        # Retorna o erro como resposta JSON, com código 500 para erro interno
        return jsonify({'error': str(e)}), 500
    

   
