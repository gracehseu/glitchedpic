from glitches.randomPixelSwap import randomPixelSwap
from glitches.MoveRowSideToSide import MoveRowSideToSide
from glitches.FlipImageAndCombine import FlipImageAndCombine
from museums.metMuseum import MetMuseumRetriever
from museums.ArtInstutitueChicago import ArtInstituteChicagoRetriever
from glitches.Anaglyph3dEffect import Anaglyph3dEffect
import random
museum_list = [MetMuseumRetriever, ArtInstituteChicagoRetriever]
glitch_list = [FlipImageAndCombine, MoveRowSideToSide, randomPixelSwap]

if __name__ == '__main__':

    source = random.choice(museum_list)()
    source.get_image()

    glitch = random.choice(glitch_list)()
    glitch.glitch_image(source.name)
