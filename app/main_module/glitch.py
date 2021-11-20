
from app.main_module.glitches.randomPixelSwap import randomPixelSwap
from app.main_module.glitches.MoveRowSideToSide import MoveRowSideToSide
from app.main_module.glitches.FlipImageAndCombine import FlipImageAndCombine
from app.main_module.museums.ArtInstutitueChicago import ArtInstituteChicagoRetriever
from app.main_module.museums.metMuseum import MetMuseumRetriever
from app.main_module.DateUtil import getTodaysDateAsString
# from glitches.Anaglyph3dEffect import Anaglyph3dEffect
from mem_top import mem_top

import random

museum_list = [MetMuseumRetriever, ArtInstituteChicagoRetriever]
glitch_list = [FlipImageAndCombine, MoveRowSideToSide, randomPixelSwap]


def createGlitchedArtWork():
    print(mem_top())
    print("creating new artwork")
    source = random.choice(museum_list)()
    # source = MetMuseumRetriever()
    source.get_image()

    glitch = random.choice(glitch_list)()
    print(glitch.image_glitch_type)
    glitch.glitch_image(getTodaysDateAsString() + ".jpeg")
    print("glitched art created")