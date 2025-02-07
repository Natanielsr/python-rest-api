from abc import ABC, abstractmethod

from services.lyric_extractor_abstract_factory.lyric_extractor import LyricExtractor

class LyricExtractorFactory(ABC):
    @abstractmethod
    def create_extractor(self) -> LyricExtractor:
        raise("implement LyricExtractorFactory create_extractor() method")