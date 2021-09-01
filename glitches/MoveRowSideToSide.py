from glitches.ImageGlitcherInterface import ImageGlitcherInterface
from PIL import Image
from scipy.ndimage import rotate
import random
import numpy as np


class MoveRowSideToSide(ImageGlitcherInterface):

    def __init__(self):
        self.image_glitch_type = "move random row from side to side"

    def glitch_image(self, image_name):
        print(str(image_name))
        # image_name = "Love of Winter.jpeg"
        im = Image.open("images/" + image_name)


        self.save_image(image_name, new_image)

    