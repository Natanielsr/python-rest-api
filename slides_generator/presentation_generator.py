from typing import List
from pptx import Presentation
from slides_generator.music import  Music
from slides_generator.slide_generator import SlideGenerator
from slides_generator.slide_data import SlideData
import traceback

class PresentationGenerator:

    def __init__(
            self,
            musics: List[Music],
            insert_title : bool = False,
            save_path : str = '',
            path_logo : str = None
        ):
        if not all(isinstance(music, Music) for music in musics):
            raise TypeError("musics parameter must be a list of Music objects")
        
        self.__musics = musics  
        self.__presentation = Presentation()
        self.__slide_layout = self.__presentation.slide_layouts[6]
        self.__insert_title : bool = insert_title
        self.save_path = save_path
        self.path_logo = path_logo

    def generate_presentation_slides(self):
        print("Generating presentation slides...")
        for music in self.__musics:
            self._generate_music_slides(music)
            self.add_blank_slide()

        print("Presentation Slides generated with Success!")
        return self.__presentation
    
    def add_blank_slide(self):
        slide_data = SlideData("", "")
        slideGen = SlideGenerator(self.__presentation, self.__slide_layout, slide_data, self.path_logo)
        slideGen.create_stanza_slide(False)

    def _generate_music_slides(self, music : Music):
        try:
            stanzas = self._separate_stanzas(music.lyrics)
            for stanza in stanzas:
                slide = SlideData(
                    music.title,
                    stanza)
            
                slideGen = SlideGenerator(self.__presentation, self.__slide_layout, slide, self.path_logo)
                slideGen.create_stanza_slide(self.__insert_title)

        except Exception as e:
            raise RuntimeError(f"Error generating slides for music {music.title}: {str(e)}")

    def _separate_stanzas(self, lyric):
        return lyric.strip().split('\n\n')
    
    def save_presentation_file(self, file_name="slides.pptx"):
        full_path = self.save_path+file_name
        print(f"Saving file...")
        self.__presentation.save(full_path)
        print(f"Presentation file saved at {full_path} with Success!")
    
    
    



    
    
    
    