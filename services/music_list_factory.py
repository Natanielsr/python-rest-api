
from dto.music_dto import MusicDTO
from services.lyric_extractor_abstract_factory.lyric_extractor_manager import LyricExtractorManager
from slides_generator.music import Music

class MusicListFactory:
    def __init__(self, musicDTO_list : list[MusicDTO]):
        
        self.music_list : list[Music] = []
        self.musicDTO_list = musicDTO_list

    def get_music_list(self) -> list[Music]:
        return self.music_list
        
    def create_music_list(self):
        try:
            for musicDTO in self.musicDTO_list:
                if musicDTO.lyric == "":
                    extractor = LyricExtractorManager(musicDTO.link)
                    lyric = extractor.get_lyric()
                    self.music_list.append(Music(musicDTO.name, lyric))
                else:
                    self.music_list.append(Music(musicDTO.name, musicDTO.lyric))

        except Exception as e:
            raise RuntimeError(f"Erro ao criar lista músicas: {e}")
