from flask import Blueprint, jsonify
from google_search import GoogleSearch

search_bp = Blueprint('search', __name__)

@search_bp.route('/search/<string:query>', methods=['GET'])
def get_search_results(query):
    site = 'site:musicasparamissa.com.br'
    
    google_search = GoogleSearch(query, site)
    try:
        links = google_search.search()
        return jsonify({'results': links})
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        # Retorna o erro como resposta JSON, com código 500 para erro interno
        return jsonify({'error': str(e)}), 500
    
   
