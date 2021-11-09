# from glitches.randomPixelSwap import randomPixelSwap
# from glitches.MoveRowSideToSide import MoveRowSideToSide
# from glitches.FlipImageAndCombine import FlipImageAndCombine
# from museums.metMuseum import MetMuseumRetriever
# from museums.ArtInstutitueChicago import ArtInstituteChicagoRetriever
from app.main_module.glitches import randomPixelSwap, MoveRowSideToSide, FlipImageAndCombine
from app.main_module.museums.ArtInstutitueChicago import ArtInstituteChicagoRetriever
from app.main_module.museums.metMuseum import MetMuseumRetriever
# from glitches.Anaglyph3dEffect import Anaglyph3dEffect
import random

museum_list = [MetMuseumRetriever, ArtInstituteChicagoRetriever]
glitch_list = [FlipImageAndCombine, MoveRowSideToSide, randomPixelSwap]


# @sched.scheduled_job('cron', id='create_new_art', hour='0', minute='1')
#
# @sched.scheduled_job('interval', id='create_new_art', minutes='*')
def createGlitchedArtWork():
    print("creating new artwork")
    source = random.choice(museum_list)()
    source.get_image()

    glitch = random.choice(glitch_list)()
    glitch.glitch_image(source.name)
    print("glitched art created")