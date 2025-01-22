from flask import Blueprint, jsonify
from services.extract_lyric import LyricExtractor
from validators.ValidateURL import ValidateURL

lyric_bp = Blueprint('lyric', __name__)

@lyric_bp.route('/lyric/<path:url>', methods=['GET'])
def get_search_results(url):

    if ValidateURL.is_valid(url) is False:
        return jsonify({'error': f'URL: "{url}" inválida ou não suportada.'}), 400

    lyric_extractor = LyricExtractor(url)
    lyric = lyric_extractor.get_lyric()
    
    return jsonify({'lyric': lyric})
