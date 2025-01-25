from services.lyric_extractor_letras import LyricExtractorLetras
from services.lyric_extractor_musicas_para_missa import LyricExtractorMusicasParaMissa
from validators.ValidateURL import ValidateURL


class LyricExtractor:
    def get_lyric(self, url: str) -> str:

        if ValidateURL.is_valid(url) is False:
            raise(f'URL: "{url}" inválida ou não suportada.')
        
        host_name = ValidateURL.get_host_name(url)
        if host_name is None:
            raise(f'Host da URL: "{url}" não suportado.')
        
        lyric = ''
        if host_name == 'letrasmus':
            lyric_extractor = LyricExtractorLetras()
            lyric = lyric_extractor.get_lyric(url)
        elif host_name == 'musicasparamissa':
            lyric_extractor = LyricExtractorMusicasParaMissa()
            lyric = lyric_extractor.get_lyric(url)

        return lyric