from services.lyric_extractor import LyricExtractor
from dto.music_dto import MusicDTO
from slides_generator.music import Music

class MusicListFactory:
    def __init__(self, musicDTO_list : list[MusicDTO]):
        self.extractor = LyricExtractor()
        self.music_list : list[Music] = []
        self.musicDTO_list = musicDTO_list

    def get_music_list(self) -> list[Music]:
        return self.music_list
        
    def create_music_list(self):
        try:
            for music in self.musicDTO_list:
                lyric = self.extractor.get_lyric(music.link)
                self.music_list.append(Music(music.name, lyric))
        except Exception as e:
            raise RuntimeError(f"Erro ao criar lista músicas: {e}")
