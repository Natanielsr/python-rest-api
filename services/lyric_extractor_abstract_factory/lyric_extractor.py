from abc import ABC, abstractmethod

#Classe abstrata LyricExtractor
class LyricExtractor(ABC):
    @abstractmethod
    def get_lyric(self, url : str) -> str :
        raise("implement LyricExtractor get_lyric() method")
