from services.lyric_extractor_abstract_factory.factory_select_config import FactorySelectConfig
from services.lyric_extractor_abstract_factory.lyric_extractor_factory import LyricExtractorFactory


class LyricExtractorManager:
    def __init__(self, url : str):
        self.factory = FactorySelectConfig().select(url)
        self.lyric_extractor = self.factory.create_extractor()
        self.url = url

    def get_lyric(self) -> str:
        return self.lyric_extractor.get_lyric(self.url)