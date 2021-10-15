from glitches.randomPixelSwap import randomPixelSwap
from glitches.MoveRowSideToSide import MoveRowSideToSide
from glitches.FlipImageAndCombine import FlipImageAndCombine
from museums.metMuseum import MetMuseumRetriever
from museums.ArtInstutitueChicago import ArtInstituteChicagoRetriever
from glitches.Anaglyph3dEffect import Anaglyph3dEffect
from glitches.SwirlImage import SwirlImage
import random
museum_list = [MetMuseumRetriever, ArtInstituteChicagoRetriever]
glitch_list = [FlipImageAndCombine, MoveRowSideToSide, randomPixelSwap, SwirlImage]

if __name__ == '__main__':

    # source = random.choice(museum_list)()
    # source.get_image()
    # print(source.name)
    # print(type(source.name))
    # glitch = random.choice(glitch_list)()
    # glitch.glitch_image(source.name)

    # test
    glitch_list[-1]().glitch_image("starrynight.jpg")