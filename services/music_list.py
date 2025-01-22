from services.extract_lyric import LyricExtractor
from dto.music_dto import MusicDTO
from slides_generator.music import Music

class MusicList:
    def __init__(self, musicDTO_list : list[MusicDTO]):
        self.extractor = LyricExtractor()
        self.music_list : list[Music] = []
        self.musicDTO_list = musicDTO_list

    def get_music_list(self):
        return self.music_list
        
    def create_music_list(self):
        try:
            for music in self.musicDTO_list:
                lyric = self.extractor.get_lyric(music.link)
                self.music_list.append(Music(music.name, lyric))
        except Exception as e:
            raise RuntimeError(f"Erro ao criar lista músicas: {e}")

if __name__ == "__main__":
    musicDTO_list = [MusicDTO("title", 'https://musicasparamissa.com.br/musica/santo-leo-mantovani/')]
    musicList = MusicList(musicDTO_list)
    musicList.create_music_list()
    print(musicList.get_music_list)