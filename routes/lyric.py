from flask import Blueprint, jsonify
from services.lyric_extractor_abstract_factory.lyric_extractor_manager import LyricExtractorManager

lyric_bp = Blueprint('lyric', __name__)

@lyric_bp.route('/lyric/<path:url>', methods=['GET'])
def get_search_results(url):

    try:
        extractor = LyricExtractorManager(url)
        lyric = extractor.get_lyric()
    except BaseException as e:
        return jsonify({'error': str(e)}), 400
    
    return jsonify({'lyric': lyric})
