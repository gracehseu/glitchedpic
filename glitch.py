from glitches.FlipImageAndCombine import FlipImageAndCombine
from museums.metMuseum import MetMuseumRetriever
from museums.ArtInstutitueChicago import ArtInstituteChicagoRetriever
from glitches.Anaglyph3dEffect import Anaglyph3dEffect
import random
museum_list = [MetMuseumRetriever, ArtInstituteChicagoRetriever]
glitch_list = [FlipImageAndCombine, Anaglyph3dEffect]

if __name__ == '__main__':

    # glitch = random.choice(museum_list)()
    source = museum_list[1]()
    source.get_image()

    # glitch = random.choice(glitch_list)()
    glitch = glitch_list[1]()
    glitch.glitch_image(source.name)
