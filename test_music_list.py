from dto.music_dto import MusicDTO
from services.music_list_factory import MusicListFactory


if __name__ == "__main__":
    musicDTO_list = [
        MusicDTO("santo", 'https://musicasparamissa.com.br/musica/santo-leo-mantovani/'),
        MusicDTO("Gloria", 'https://www.letras.mus.br/agnus-dei/901672/'),
    ]
    mlf = MusicListFactory(musicDTO_list)
    mlf.create_music_list()

    for music in mlf.get_music_list():
        print('title: ', music.title)
        print('lyrics:', music.lyrics)
        print()