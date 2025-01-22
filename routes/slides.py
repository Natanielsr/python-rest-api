from flask import Blueprint, jsonify, request

from dto.MusicDTO import MusicDTO
from validators.ValidateURL import ValidateURL
from werkzeug.exceptions import BadRequest

slides_bp = Blueprint('slides', __name__)

@slides_bp.route('/slides/generate/', methods=['POST'])
def generate_slides():
    try:
        data = request.get_json()
        validate_data(data)
        params = data.get('params')
        music_list = get_music_list(params)
    except BadRequest as e:
        return jsonify({'error': e.description}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    #TODO Implementar a geração dos slides

    # Processa os dados conforme necessário
    return jsonify({'slides': 'slides', 'received_data': [music.to_dict() for music in music_list]})

def validate_data(data):
    if 'params' not in data:
        raise BadRequest(description='Parâmetros não encontrados')

def get_music_list(params) : 
    music_list = []
    for param in params:
        if not isinstance(param, dict):
            raise BadRequest(description='Cada parâmetro deve ser um objeto')
        if 'name' not in param or 'link' not in param:
            raise BadRequest(description='Cada parâmetro deve conter "name" e "link"')

        print(param['link'])
        if ValidateURL.is_valid(param['link']) is False:
            raise BadRequest(description=f'Link ({param["link"]}) inválido')
        
        music = MusicDTO(param['name'], param['link'])
        music_list.append(music)

    return music_list