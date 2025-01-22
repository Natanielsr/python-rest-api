#from music_list import MusicList
from presentation_generator import PresentationGenerator
from music import Music

if __name__ == "__main__":

    #music_txt_folder = './musics/'
    #musics = MusicList(music_txt_folder).get_music_list()

    #print (musics)

    musics = [Music("title", "first line\n\nsecond line")]
    
    slideGen = PresentationGenerator(musics, False, 'slide_file/')
    slideGen.generate_presentation_slides()
    slideGen.save_presentation_file()