from flask import Blueprint, jsonify
from services.lyric_extractor import LyricExtractor
from validators.ValidateURL import ValidateURL

lyric_bp = Blueprint('lyric', __name__)

@lyric_bp.route('/lyric/<path:url>', methods=['GET'])
def get_search_results(url):

    try:
        extractor = LyricExtractor()
        lyric = extractor.get_lyric(url)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
    return jsonify({'lyric': lyric})
