class Music:
    def __init__(self, title : str, lyrics : str):
        self.title = title
        self.lyrics = lyrics
        
    # Método para comparação de igualdade
    def __eq__(self, other):
        if isinstance(other, Music):
            return self.title == other.title and self.lyrics == other.lyrics
        return False
    
    def to_dict(self):
        return {'title': self.title, 'content': self.lyrics}