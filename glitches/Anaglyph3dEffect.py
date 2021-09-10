from glitches.ImageGlitcherInterface import ImageGlitcherInterface
from PIL import Image
from scipy.ndimage import rotate
import random
import numpy as np


class Anaglyph3dEffect(ImageGlitcherInterface):

    def __init__(self):
        self.image_glitch_type = "anaglyph 3d effect"

    def glitch_image(self, image_name):
        print(str(image_name))
        image_name = "Love of Winter.jpeg"
        im = Image.open("images/" + image_name).convert('RGB')


        r, g, b = im.split()

        r = np.array(r)
        g = np.array(g)
        b = np.array(b)

        r = np.roll(r, -20)
        r = np.roll(r, -20, axis = 0)

        b = np.roll(b, 20)
        b = np.roll(b, 20, axis = 0)

        print(len(r), len(r[0]))
        print(len(b), len(b[0]))
        print(r[0])

        

        new_image = Image.merge('RGB', (red, green, blue))
        self.save_image(image_name, new_image)

    