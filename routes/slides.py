import uuid
from flask import Blueprint, jsonify, request, send_from_directory
from dto.music_dto import MusicDTO
from services.music_list_factory import MusicListFactory
from slides_generator.music import Music
from slides_generator.presentation_generator import PresentationGenerator
from validators.ValidateURL import ValidateURL
from werkzeug.exceptions import BadRequest

slides_bp = Blueprint('slides', __name__)

@slides_bp.route('/slides/generate/', methods=['POST'])
def generate_slides():
    try:
        data = request.get_json()
        validate_data(data)
        params = data.get('params')
        music_list_dto : MusicDTO = get_music_list(params)

        ml = MusicListFactory(music_list_dto)
        ml.create_music_list()
        music_list : list[Music] = ml.get_music_list()
        path = 'slide_file/'
        path_logo = 'images/icon.png'

        prs = PresentationGenerator(music_list, False, path, path_logo)
        prs.generate_presentation_slides()
        file_name = str(uuid.uuid4().hex) + '.pptx'
        prs.save_presentation_file(file_name)

        host_url = request.host_url
        if not ("localhost" in host_url or "127.0.0.1" in host_url):
            host_url = host_url.replace("http://", "https://")

    except BadRequest as e:
        return jsonify({'error': e.description}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


    # Processa os dados conforme necessário
    return jsonify({
        'message': 'Slides generated successfully',
        'file_url': host_url + 'slides/download/' + file_name,
        'file_name': file_name
    })

@slides_bp.route('/slides/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        return send_from_directory('slide_file', filename, as_attachment=True)
    except FileNotFoundError:
        return jsonify({'error': 'Arquivo não encontrado'}), 404

def validate_data(data):
    if 'params' not in data:
        raise BadRequest(description='Parâmetros não encontrados')

def get_music_list(params) -> MusicDTO: 
    music_list = []
    for param in params:
        if not isinstance(param, dict):
            raise BadRequest(description='Cada parâmetro deve ser um objeto')
        if 'name' not in param or 'link' not in param:
            raise BadRequest(description='Cada parâmetro deve conter "name" e "link"')

        if ValidateURL.is_valid(param['link']) is False:
            raise BadRequest(description=f'Link ({param["link"]}) inválido')
        
        music = MusicDTO(param['name'], param['link'])
        music_list.append(music)

    return music_list