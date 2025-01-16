from flask import Blueprint, jsonify
from services.extract_lyric import LyricExtractor

lyric_bp = Blueprint('lyric', __name__)

@lyric_bp.route('/lyric/<path:url>', methods=['GET'])
def get_search_results(url):

    if not url.startswith('https://musicasparamissa.com.br/musica/'):
        return jsonify({'error': 'URL inválida ou não suportada.'}), 400

    lyric_extractor = LyricExtractor(url)
    lyric = lyric_extractor.get_lyric()
    
    return jsonify({'lyric': lyric})
