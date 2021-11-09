
from app.main_module.glitches import randomPixelSwap, MoveRowSideToSide, FlipImageAndCombine
from app.main_module.museums.ArtInstutitueChicago import ArtInstituteChicagoRetriever
from app.main_module.museums.metMuseum import MetMuseumRetriever
# from glitches.Anaglyph3dEffect import Anaglyph3dEffect
import random

museum_list = [MetMuseumRetriever, ArtInstituteChicagoRetriever]
glitch_list = [FlipImageAndCombine, MoveRowSideToSide, randomPixelSwap]


def createGlitchedArtWork():
    print("creating new artwork")
    source = random.choice(museum_list)()
    source.get_image()

    glitch = random.choice(glitch_list)()
    glitch.glitch_image(source.name)
    print("glitched art created")