class MusicDTO:
    def __init__(self, name, link, lyric):
        self.name = name
        self.link = link
        self.lyric = lyric

    def to_dict(self):
        return {'name': self.name, 'link': self.link, 'lyric': self.lyric}